#!/usr/bin/env python3
"""
Digital Life System — Memory Backup Tool
沙海数字生命系统 — 记忆备份工具

Usage / 使用方法:
    python memory_backup.py backup      # 执行完整备份 / Run full backup
    python memory_backup.py restore     # 从最新快照恢复 / Restore from latest snapshot
    python memory_backup.py status      # 查看当前备份状态 / Check backup status
    python memory_backup.py list        # 列出所有历史快照 / List all snapshots
"""

import os
import sys
import shutil
import zipfile
import datetime
import json
from pathlib import Path

# ============================================================
# 配置 / Configuration
# ============================================================

# 当前脚本所在目录 / Directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()

# memory 目录路径（相对于脚本所在目录）/ memory directory path
MEMORY_DIR = SCRIPT_DIR / "memory"

# 备份目录 / Backup directory
BACKUP_DIR = SCRIPT_DIR.parent / "memory-backup"

SNAPSHOTS_DIR = BACKUP_DIR / "snapshots"
MANIFEST_FILE = BACKUP_DIR / "LATEST_MANIFEST.txt"

BACKUP_NAME_PREFIX = "memory"
MAX_SNAPSHOT_AGE_DAYS = 90


# ============================================================
# 辅助函数 / Helper Functions
# ============================================================

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")


def ensure_dirs():
    SNAPSHOTS_DIR.mkdir(parents=True, exist_ok=True)


def get_snapshot_files():
    if not SNAPSHOTS_DIR.exists():
        return []
    return sorted(SNAPSHOTS_DIR.glob(f"{BACKUP_NAME_PREFIX}_*.zip"), reverse=True)


def get_latest_snapshot():
    snapshots = get_snapshot_files()
    return snapshots[0] if snapshots else None


# ============================================================
# 备份操作 / Backup Operations
# ============================================================

def run_backup():
    """执行完整备份（三层同时执行）"""
    ensure_dirs()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_path = SNAPSHOTS_DIR / f"{BACKUP_NAME_PREFIX}_{timestamp}.zip"

    # 第1层：创建 ZIP 快照
    log(f"创建 ZIP 快照... / Creating ZIP snapshot...")
    with zipfile.ZipFile(snapshot_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in MEMORY_DIR.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(MEMORY_DIR)
                zf.write(file_path, arcname)

    size = snapshot_path.stat().st_size / 1024
    log(f"✅ ZIP 快照已创建：{snapshot_path.name} ({size:.1f} KB)")

    # 第2层：生成纯文本恢复清单
    log(f"生成纯文本恢复清单... / Generating text manifest...")
    manifest_lines = [
        f"# Memory Backup Manifest / 记忆备份清单",
        f"# Generated at / 生成时间：{timestamp}",
        f"# Snapshot / 快照文件：{snapshot_path.name}",
        "",
    ]

    for file_path in sorted(MEMORY_DIR.rglob("*")):
        if file_path.is_file():
            rel_path = str(file_path.relative_to(MEMORY_DIR))
            manifest_lines.append(f"\n--- FILE: {rel_path} ---")
            try:
                content = file_path.read_text(encoding="utf-8")
                manifest_lines.append(content)
            except Exception as e:
                manifest_lines.append(f"[ERROR reading file: {e}]")

    MANIFEST_FILE.write_text("\n".join(manifest_lines), encoding="utf-8")
    log(f"✅ 纯文本清单已生成：{MANIFEST_FILE.name}")

    # 清理旧快照
    log("清理超过90天的旧快照... / Cleaning old snapshots...")
    cleaned = 0
    for old in get_snapshot_files()[MAX_SNAPSHOT_AGE_DAYS:]:
        old.unlink()
        log(f"  🗑️  删除：{old.name}")
        cleaned += 1
    if cleaned == 0:
        log("  无需清理的旧快照 / No old snapshots to clean")

    log("✅ 备份完成！/ Backup complete!")


def run_restore():
    """从最新快照恢复"""
    latest = get_latest_snapshot()
    if not latest:
        log("❌ 没有找到快照，无法恢复。/ No snapshot found, cannot restore.")
        return

    log(f"找到最新快照：{latest.name}")
    log(f"警告：此操作将覆盖当前 memory/ 目录！")
    confirm = input("确认恢复？(y/N) / Confirm restore? (y/N): ")
    if confirm.lower() != "y":
        log("取消恢复 / Restore cancelled")
        return

    # 清空现有 memory 目录
    if MEMORY_DIR.exists():
        shutil.rmtree(MEMORY_DIR)
    MEMORY_DIR.mkdir(parents=True)

    # 解压快照
    with zipfile.ZipFile(latest, "r") as zf:
        zf.extractall(MEMORY_DIR)

    log(f"✅ 已从 {latest.name} 恢复到 memory/")


def run_status():
    """查看备份状态"""
    log("=== 备份状态 / Backup Status ===")

    # memory 目录
    if MEMORY_DIR.exists():
        file_count = sum(1 for _ in MEMORY_DIR.rglob("*") if _.is_file())
        size = sum(f.stat().st_size for f in MEMORY_DIR.rglob("*") if f.is_file()) / 1024
        log(f"memory/ 文件数：{file_count}，总大小：{size:.1f} KB")
    else:
        log("⚠️  memory/ 目录不存在 / memory/ directory does not exist")

    # 备份目录
    if BACKUP_DIR.exists():
        snapshot_count = len(get_snapshot_files())
        log(f"快照数量：{snapshot_count}")

        if MANIFEST_FILE.exists():
            mtime = datetime.datetime.fromtimestamp(MANIFEST_FILE.stat().st_mtime)
            log(f"最新清单：{mtime.strftime('%Y-%m-%d %H:%M')}")
    else:
        log("⚠️  备份目录不存在 / Backup directory does not exist")

    # 最新快照
    latest = get_latest_snapshot()
    if latest:
        mtime = datetime.datetime.fromtimestamp(latest.stat().st_mtime)
        size = latest.stat().st_size / 1024
        log(f"最新快照：{latest.name} ({size:.1f} KB, {mtime.strftime('%Y-%m-%d %H:%M')})")
    else:
        log("⚠️  暂无快照 / No snapshots yet")


def run_list():
    """列出所有历史快照"""
    snapshots = get_snapshot_files()
    if not snapshots:
        log("暂无快照 / No snapshots")
        return

    log(f"共 {len(snapshots)} 个快照：")
    for s in snapshots:
        mtime = datetime.datetime.fromtimestamp(s.stat().st_mtime)
        size = s.stat().st_size / 1024
        marker = " ← 最新" if s == snapshots[0] else ""
        log(f"  {s.name} ({size:.1f} KB, {mtime.strftime('%Y-%m-%d %H:%M')}){marker}")


# ============================================================
# 入口 / Entry Point
# ============================================================

if __name__ == "__main__":
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else ""

    if cmd == "backup":
        run_backup()
    elif cmd == "restore":
        run_restore()
    elif cmd == "status":
        run_status()
    elif cmd == "list":
        run_list()
    else:
        print(__doc__)
