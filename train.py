import pyrootutils

ROOT = pyrootutils.setup_root(
    search_from=__file__,
    indicator=["requirements.txt"],
    pythonpath=True,
    dotenv=True,
)

import yaml
from yaml.loader import SafeLoader
from pathlib import Path
from misc import train

# comet
import comet_ml
from comet_ml import Experiment


def read_config(config):
    with open(f'{config}', 'r') as f:
        data = list(yaml.load_all(f, Loader=SafeLoader))
    # print(data[0]['params'])
    return data[0]['params']

def main(**kwargs):
    config = read_config(kwargs["config"])
    opt = train.parse_opt(True)
    for k, v in config.items():
        if k in ["weights", "data"]:
            v = Path(ROOT, v)
        setattr(opt, k, v)
    
    # experiment = Experiment(
    #     api_key='7DE8EZJwDwczUd8gpo7zOOpwz',
    #     project_name='example',
    #     workspace="danielsyahputra"
    # )
    # experiment.set_name(opt.name)
    # train.main(opt)
    print(opt)

if __name__=="__main__":

    main(config="configs/config.yaml")