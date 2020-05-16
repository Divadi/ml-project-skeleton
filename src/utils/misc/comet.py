import os
import comet_ml

#! Gets asset with asset_name from comet, 
#! Saves it locally, and returns path to saved file
def get_asset(project_name, experiment_name, asset_name):
    comet_api = comet_ml.api.API(api_key=os.environ['COMET_API_KEY'])
    experiment = comet_api.get_experiment(
        workspace="jinhyun1", 
        project_name=project_name, 
        experiment=experiment_name
    )
    assets = experiment.get_asset_list() # list of dictionaries, each an asset.
    asset_id = None
    for d in assets:
        if d['fileName'] == asset_name:
            asset_id = d['assetId']
            break
    if asset_id == None:
        raise Exception("Provided asset_name not found")

    asset_binary = experiment.get_asset(asset_id)

    res_path = "/tmp/{}".format(asset_name)
    with open(res_path, "wb") as f:
        f.write(asset_binary)
    
    return res_path