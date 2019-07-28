# ProgramName:ImageOrganizingProgram
# Ver:1.01
# Creation Date:2019/07/23
# Make Program:Yuuma

# 必要なライブラリのインポート
import codecs
import datetime
import json
import os
import shutil
import matplotlib.pyplot as plot
import numpy
# インポート終わり


# 必要な関数の記述
def save_log(
        log_folder_path: str,
        log_message: str
):
    try:
        log_file_name = "{0}_log.txt".format(get_date_data())
        with codecs.open(filename=log_folder_path + log_file_name, mode="a", encoding="utf-8") as log_file:
            log_file.write(log_message)
            log_file.close()
    except Exception as save_log_error:
        print(save_log_error)
        exit()


def get_time_stamp():
    now = datetime.datetime.now()
    time_stamp: str = "{hour}_{minute}_{second}_{micro_second}".format(
        hour="0"+str(now.hour) if int(now.hour) < 10 else str(now.hour),
        minute="0"+str(now.minute) if int(now.minute) < 10 else str(now.minute),
        second="0"+str(now.second) if int(now.second) < 10 else str(now.second),
        micro_second=str(now.microsecond)
    )
    return time_stamp


def get_date_data(

):
    today_data: datetime.date = datetime.date.today()
    date_data: str = "{year}_{month}_{day}".format(
        year="0" + str(today_data.year) if today_data.year < 10 else str(today_data.year),
        month="0" + str(today_data.month) if today_data.month < 10 else str(today_data.month),
        day="0" + str(today_data.day) if today_data.day < 10 else str(today_data.day)
    )
    return date_data


def error_check(
        error_occurred: bool,
):
    if error_occurred:
        exit()


def check_image(
        file_name: str,
        image_extension: list
):
    return file_name.split(".")[-1] in image_extension
# 必要な関数の記述終わり

#########################################
# 変数規則 所属処理_変数の種類_変数が指すもの#
#########################################
# main:m ################################
#########################################


m_config_path: str = "config.json"
m_config_data: dict = {}

m_log_folder_path: str = "./log/"
m_log_message: str = ""

m_error_occurred: bool = False

# loadConfig:lc
try:
    with codecs.open(filename=m_config_path,
                     mode="r",
                     encoding="utf-8") as lc_config_file:
        m_config_data = json.load(fp=lc_config_file)
except Exception as lc_error:
    m_log_message = "{time_stamp}:Error:load config:{error}".format(error=lc_error, time_stamp=get_time_stamp())
    save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
    m_error_occurred = True
error_check(error_occurred=m_error_occurred)
# End:lc

# loadConfigJson:lcj
lcj_before_path = m_config_data["BeforePath"]
lcj_after_path = m_config_data["AfterPath"]
lcj_image_extension: list = m_config_data["ImageExtension"]
# END:lcj

# MakeDateFolder:mk
mi_file_list: list = os.listdir(path=lcj_before_path)
mi_date_folder_path = "{0}\\{1}".format(lcj_after_path, get_date_data())
if not os.path.exists(path=mi_date_folder_path):
    try:
        os.mkdir(path=mi_date_folder_path)
        m_log_message = "{time_stamp}:MoveImage/MakeDateFolder:{folder_name}\n".format(
            time_stamp=get_time_stamp(),
            folder_name=get_date_data()
        )
        save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)

    except Exception as im_md_error:
        m_log_message = "{time_stamp}:Error:MoveImage/MakeDateFolder:{error}\n".format(
            error=im_md_error,
            time_stamp=get_time_stamp()
        )
        save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
        m_error_occurred = True
    error_check(error_occurred=m_error_occurred)
# END:mk

# MoveImage:mi
for mi_image in mi_file_list:
    if check_image(file_name=mi_image, image_extension=lcj_image_extension):
        mi_image_path = "{0}\\{1}".format(lcj_before_path, mi_image)
        mi_all_folder_path = "{0}\\ALL".format(lcj_after_path)
        mi_date_folder_path = "{0}\\{1}".format(lcj_after_path, get_date_data())
        mi_move_all_folder_path = "{0}\\{1}".format(mi_all_folder_path, mi_image)
        mi_move_date_folder_path = "{0}\\{1}".format(mi_date_folder_path, mi_image)
        # MoveImage/RemoveFile:mi_rf
        if os.path.exists(path=mi_move_all_folder_path):
            try:
                os.remove(path=mi_image_path)
                m_log_message = "{time_stamp}:mi_remove:{file_name}\n".format(
                    file_name=mi_image,
                    time_stamp=get_time_stamp()
                )
                save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)

            except Exception as im_rf_error:
                m_log_message = "{time_stamp}:Error:ImageMove/RemoveFile:{error}\n".format(
                    error=im_rf_error,
                    time_stamp=get_time_stamp()
                )
                save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
                m_error_occurred = True
            error_check(m_error_occurred)
            continue
        # EMD mi_rf
        # MoveImage/MakeDateFolder:mi_md
        # END:mi_md
        # MoveImage/MoveALLFolder:mi_mAF
        try:
            shutil.copy(src=mi_image_path, dst=mi_move_all_folder_path)
            m_log_message = "{time_stamp}:MoveImage/MoveALLFolder:{file_name}\n".format(
                file_name=mi_image,
                time_stamp=get_time_stamp()
            )
            save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
        except Exception as mi_mAF_error:
            m_log_message = "{time_stamp}:Error:MoveImage/MoveImageALLFolder:{error}\n".format(
                error=mi_mAF_error,
                time_stamp=get_time_stamp())
            save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
            m_error_occurred = True
        error_check(error_occurred=m_error_occurred)
        # END:mi_mA
        # MoveImage/MoveDATEFolder:mi_mDF
        try:
            shutil.move(src=mi_image_path, dst=mi_move_date_folder_path)
            m_log_message = "{time_stamp}:MoveImage/MoveDATEFolder:{file_name}\n".format(
                file_name=mi_image,
                time_stamp=get_time_stamp()
            )
            save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
        except Exception as mi_mDF_error:
            m_log_message = "{time_stamp}:Error:MoveImage/MoveImageDATEFolder:{error}\n".format(
                error=mi_mDF_error,
                time_stamp=get_time_stamp()
            )
            save_log(log_folder_path=m_log_folder_path, log_message=m_log_message)
            m_error_occurred = True
        error_check(error_occurred=m_error_occurred)
        # END:mi_mA
# END:mi
# END Main
# Plot:p
p_Horizontal_list: list = []
p_Vertical_list: list = []
p_folder_list = os.listdir(path=lcj_after_path)
p_folder_count = 0
p_folder_limit = m_config_data["GraphLimit"]
# Plot/SetList:p_sl
for p_sl_folder in p_folder_list:
    p_sl_image_counter: int = 0
    if p_sl_folder != "ALL":
        p_folder_count += 1
        # Plot/SetList/CountImage:p_sl_ci
        p_sl_folder_path = "{0}\\{1}".format(lcj_after_path, p_sl_folder)
        for p_sl_ci_image in os.listdir(path=p_sl_folder_path):
            if check_image(file_name=p_sl_ci_image, image_extension=lcj_image_extension):
                p_sl_image_counter += 1
        p_Horizontal_list.append(p_sl_image_counter)
        p_Vertical_list.append(p_sl_folder[-5:])
        if p_folder_count == p_folder_limit:
            break
        # END p_sl_ci
p_Vertical = numpy.array(p_Vertical_list)
p_Horizontal = numpy.array(p_Horizontal_list)
# END p_sl
# Plot/viewPlot:p_v
plot.plot(p_Vertical, p_Horizontal)
p_v_save_image_path = m_config_data["PlotImagePath"]
p_v_save_image_file_path = "{0}//{1}.png".format(p_v_save_image_path, get_date_data())
plot.savefig(p_v_save_image_file_path)
# END p_v
