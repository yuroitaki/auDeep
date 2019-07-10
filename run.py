import importlib
from pathlib import Path

from audeep.backend.parsers.base import Parser


def take_action(**kwargs):
    module_name, class_name = kwargs.get("parser").rsplit(".", 1)
    parser_class = getattr(importlib.import_module(module_name), class_name)

    if not issubclass(parser_class, Parser):
        raise ValueError("specified parser does not inherit audeep.backend.parsers.Parser")

    parser = parser_class(
        kwargs.get('base_dir'),
        kwargs.get('audio_type'),
    )

    if not parser.can_parse():
        raise ValueError("specified parser is unable to parse data set at {}".format(kwargs.basedir))

    lengths = []
    sample_rates = []
    channels = []

    non_seekable_files = False

    instance_metadata = parser.parse()


def main():

    base_dir = Path("../fma_data/fma_small")
    take_action(
        parser="audeep.backend.parsers.no_metadata.NoMetadataParser",
        base_dir=base_dir,
        audio_type="mp3",
    )

if __name__ == "__main__":
    main()