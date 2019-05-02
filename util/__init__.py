import os
from datetime import datetime


def delete_excess_files(directory, max, logger):
    """
    Delete excess files in directory, if amount more than max, starts with first file(may be incorrect in some OS)
    """
    cur_files_amount = -1
    try:
        files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
        files_amount = len(files)
        cur_files_amount = files_amount
        while cur_files_amount >= max:
            os.remove(os.path.join(directory, files[0]))
            files = [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]
            cur_files_amount = len(files)
    except:
        logger.log_info("Excess files in '{}' directory was not deleted correctly, {} files left"
                        .format(directory, cur_files_amount))
    else:
        logger.log_info("From directory '{}' has been removed {} files. {} files left"
                         .format(directory, files_amount - cur_files_amount, cur_files_amount))


def get_date_file_name(extension):
    """
    Format 'now' datetime and create file name
    with a given extension like this: 'YYYY_MM_DD hh_mm_ss.ext'
    """
    return "{}.{}".format(datetime.now().replace(microsecond=0), extension).replace(":", "_")


def join_pathes(*pathes):
    result = ""
    for path in pathes:
        result = os.path.join(result, path)
    return result
