import argparse
from huro_lib.StringToObject import StringToObject
import json
from entry import step

def main():
    parser = argparse.ArgumentParser(description="Calculate square velocity.")
    parser.add_argument("json_str", type=str, help="object data")
    args = parser.parse_args()
    scene_data = StringToObject(args.json_str)
    newVelocity = json.dumps(step(scene_data))
    print(newVelocity)


if __name__ == "__main__":
    main()