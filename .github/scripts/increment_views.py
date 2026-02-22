#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print('Usage: increment_views.py <json_path> <page_path>')
        sys.exit(2)
    json_path = Path(sys.argv[1])
    page = sys.argv[2]
    if not json_path.exists():
        data = {}
    else:
        try:
            data = json.loads(json_path.read_text(encoding='utf-8'))
        except Exception:
            data = {}

    # normalize key: use page path as given
    key = page
    value = int(data.get(key, 0)) + 1
    data[key] = value

    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Updated {key} -> {value}')

if __name__ == '__main__':
    main()
