from pathlib import Path
import json,sys
root=Path(__file__).resolve().parent.parent
items=json.loads((root/'docs/ASSET_MANIFEST.json').read_text(encoding='utf-8'))['assets']
missing=[x['path'] for x in items if not (root/'game'/x['path']).is_file()]
for name in missing:print(name)
print(f"Missing {len(missing)} of {len(items)} asset files. Supply only assets you can lawfully distribute.")
sys.exit(bool(missing))
