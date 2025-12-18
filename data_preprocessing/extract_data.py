from pathlib import Path

def extract_data():
    base_path = Path("D:\Traffic_visulization\datasets")
    folder_name = '02_TransCAD_results'
    target_name = 'LinkFlows.csv'
    data_dict = {}
    for area in base_path.iterdir():
        if area.is_dir():
            data_dict[area.name] = base_path / area / folder_name / target_name
    return data_dict