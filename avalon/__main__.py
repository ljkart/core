import argparse

from . import pipeline


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--creator", action="store_true",
                        help="Launch Instance Creator in standalone mode")
    parser.add_argument("--loader", action="store_true",
                        help="Launch Asset Loader in standalone mode")
    parser.add_argument("--manager", action="store_true",
                        help="Launch Manager in standalone mode")
    parser.add_argument("--projectmanager", action="store_true",
                        help="Launch Manager in standalone mode")
    parser.add_argument("--root",
                        help="Absolute path to root directory of assets")

    args, unknown = parser.parse_known_args()
    host = pipeline.debug_host()
    pipeline.register_host(host)

    if args.creator:
        from .tools import creator
        creator.show(debug=True)

    elif args.loader:
        from .tools import loader
        loader.show(debug=True)

    elif args.manager:
        from .tools import manager
        manager.show(debug=True)

    elif args.projectmanager:
        from .tools import projectmanager
        projectmanager.cli(unknown)
