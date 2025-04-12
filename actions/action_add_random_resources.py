import logging

from operation_modules.resource_operations_remaster.add_random_resources import add_random_resources



def action_add_random_resources(source_folder,destination_folder,input_file):

    add_random_resources(source_folder_=source_folder,
                         destination_folder_=destination_folder,
                         input_file_=input_file)

if __name__ == "__main__":
    action_add_random_resources(
        source_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\source_data",
        destination_folder=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\destination_data",
        input_file=r"D:\graduate_design\example1\operation_modules\resource_operations_remaster\test_sample\sample1.exe",
        )
