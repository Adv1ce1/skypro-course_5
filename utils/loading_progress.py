import sys

def show_loading_progress(completed_items, total_items) -> None:
    animation_chars = "|/-\\"
    progress = (completed_items / total_items) * 100
    sys.stdout.write(
        f"\rЗагрузка данных... [{animation_chars[completed_items % len(animation_chars)]}] {int(progress)}%")
    sys.stdout.flush()
