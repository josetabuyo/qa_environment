# -*- coding: utf-8 -*-
from datetime import datetime
import os, json, time, re
import shutil

execution_timestamp = None
auditor_start_time = None

class Auditor:
    
    # static contructor begin
    with open(os.path.dirname(__file__) + os.sep + "auditor_config.json", encoding='utf-8') as config_file:
        config = json.load(config_file)
    
    file_name = ""
    
    # static contructor end
    
    @staticmethod
    def set_timestamp(start_time):
        global execution_timestamp
        global auditor_start_time
        execution_timestamp = str(start_time.strftime(Auditor.config['execution_timestamp_format']))
        auditor_start_time = time.time()
    
    @staticmethod
    def get_timestamp():
        global execution_timestamp
        
        if execution_timestamp == None:
            Auditor.set_timestamp(datetime.now())
        
        return execution_timestamp
    
    @staticmethod
    def set_test_name(test_name):
        Auditor.file_name = test_name
        
    @staticmethod
    def get_test_name():
        if Auditor.file_name == "":
            last_stack_trace_entry = Auditor.get_stack_trace()[-1]
            test_name = last_stack_trace_entry.split(", in ")[1]
        else:
            test_name = Auditor.file_name
            
        
        return test_name
    
    @staticmethod
    def get_log_files_location():
        from pathlib import Path
        
        log_files_location = Auditor.config['log_files_location']
        
        if log_files_location == "":
            log_files_location = str(Path(__file__).parent.parent.parent)

            log_files_location += os.sep + "output"
        
        return log_files_location
    
        
    @staticmethod
    def get_base_file_path():
        last_stack_trace_entry = Auditor.get_stack_trace()[-1]
        
        log_file_name_split = last_stack_trace_entry.split(".py")[0].split(os.sep)[-6:]

        
        log_file_name_split.append(Auditor.get_test_name())

        log_file_name = os.sep.join(log_file_name_split)
        
        return log_file_name
    
    @staticmethod   
    def get_log(log_entry, options, mode="default"):
        
        try:
            output = options['mask_'+mode].replace("<log_entry>", str(log_entry))
        except KeyError:
            # if 'mask_'+mode doesn't exists then we don't log
            output = None
        
        return output
    
    @staticmethod   
    def get_method_as_text():
        import inspect
        return  inspect.stack()[1].function.replace("_", " ")
    
    @staticmethod
    def get_filename_as_text(except_words="Component"):
        import inspect
        
        output = inspect.stack()[1].filename.split(os.sep)[-1].replace(".py", "")
        for replace_word in except_words.split(","):
            output = output.replace(replace_word, "")
        
        
        import re
        
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', output)
        output = " ".join([m.group(0) for m in matches])
        
        return output
    
    @staticmethod
    def get_stack_trace():
        import traceback
        
        stack_trace_list = list(reversed(traceback.format_stack()))


        stack_trace_own = []
        for stack_trace_item in stack_trace_list:
            
            if (
                ("tests" in stack_trace_item) or 
                ("rpa" not in stack_trace_item)
            ):
            
                stack_trace_own.append(stack_trace_item.split("\n")[0])
            else:
                continue
        
        return stack_trace_own
    
    
    @staticmethod
    def method_call_to_text(method_name, args, kwargs):
        text = method_name.replace("_", " ")
            
            
        args_to_print = []
        
        try:
            for arg in args:
                if type(arg) == str:
                    args_to_print.append(arg)
                
                if type(arg) == int:
                    args_to_print.append(str(arg))
                
                #if type(arg) == dict:
                #    args_to_print.append(json.dumps(arg))
        
        except TypeError:
            pass
        
        
        if args_to_print:
            text+=" - {}".format(" ".join(args_to_print))
            
            
        if kwargs:
            text+=" - {}".format(" ".join("{}: {}".format(key, value) for key, value in kwargs.items()))
        
        
        return text
    
    @staticmethod
    def get_log_file_path_with_timestamp(log_output_config):
        log_files_location = Auditor.get_log_files_location()
        base_file_path = Auditor.get_base_file_path()
        
        folder = os.sep.join([
            log_files_location,
            log_output_config['sub_folder']
        ])
        
        log_file_path = "{}{}{}_{}{}".format(
            folder,
            os.sep,
            base_file_path,
            Auditor.get_timestamp(),
            log_output_config['extension']
        )
        return log_file_path
    
    @staticmethod
    def get_log_file_path_unique(log_output_config):
        log_files_location = Auditor.get_log_files_location()
        base_file_path = Auditor.get_base_file_path()
        
        folder = os.sep.join([
            log_files_location,
            log_output_config['sub_folder']
        ])
        
        log_file_path = "{}{}{}{}".format(
            folder,
            os.sep,
            base_file_path,
            log_output_config['extension']
        )
        return log_file_path
    
    @staticmethod
    def clean_unique_files(log_output_config):
        from os import listdir
        
        file_path = Auditor.get_log_file_path_with_timestamp(log_output_config)
        file_path_unique = Auditor.get_log_file_path_unique(log_output_config)
        
        folder = os.sep.join(file_path.split(os.sep)[:-1])
        
        for file_name in listdir(folder):
            log_output_config['extension']
            
            file_unique = file_path_unique.split(os.sep)[-1]
            
            file_base = file_unique.replace(log_output_config['extension'], "")
            
            if (file_base in file_name) and (file_name != file_unique):
                print("remove non-unique filenames")
                print(folder + os.sep + file_name)
            
                os.remove(folder + os.sep + file_name)

                
    
    
    @staticmethod
    def get_tickets_from_test_name(test_name):
        tickets = []
        
        matches = re.findall('[_]C[0-9]+', test_name)
        
        for m in matches:
            ticket = m.replace("_", "").replace("C", "")
            tickets.append(ticket)
        
        return tickets
    



    @staticmethod
    def close_reports(result_text):
        date_time_obj = datetime.strptime(Auditor.get_timestamp(), '%Y%m%d_%H%M%S')
        test_start_time = datetime.timestamp(date_time_obj)
        elapsed_time = time.time() - test_start_time
        
        log("""
##################################################################
Result: {}
Elapsed time: {} s
##################################################################
""".format(
        result_text,
        round(elapsed_time, 2)
    ), mode="title")
        
        filename = None
        
        report_path_text = "Reports:"
        
        for log_output in Auditor.config['log_outputs']:
            log_output_config =  Auditor.config['log_outputs'][log_output]
            
            if 'expected_result' in log_output_config:
                if log_output_config['expected_result'] != result_text:
                    continue
            
            if 'extension' in log_output_config:
                #it is a file kind output
                
                
                filename = Auditor.get_log_file_path_with_timestamp(log_output_config)
                
                if log_output_config['unique']:
                    target_filename = Auditor.get_log_file_path_unique(log_output_config)
                    
                    shutil.move(filename, target_filename)
                    
                    Auditor.clean_unique_files(log_output_config)
                    
                    filename = target_filename

                report_path_text += "\n- {}: {}".format(log_output, filename)
        
             
        print(report_path_text)
        return None
    
def log(log_entry, test_instance=None, mode="default"):
    global execution_timestamp
    if execution_timestamp == None:
        Auditor.set_timestamp(datetime.now())
    
    log_entry_separator = Auditor.config['log_entry_separator']
    
    try:
        base_file_path = Auditor.get_base_file_path()
    except:
        print(log_entry)
        return

    log_files_location = Auditor.get_log_files_location()
    
    
    if test_instance:
        try:
            if test_instance.errorLib and mode == "assert" and test_instance.screenshot_generation_switch:
                test_instance.screenshot_loc = test_instance.errorLib.generate_a_screenshot(test_instance.screenshot_counter)
                test_instance.screenshot_counter += 1
        except:
            None

    for log_output in Auditor.config['log_outputs']:
        try:

            log_output_config =  Auditor.config['log_outputs'][log_output]
            log_entry_enritched = Auditor.get_log(log_entry, log_output_config, mode)
            if log_entry_enritched is None or log_entry_enritched == "": continue
            
            if(log_output_config['stack_trace'] == "true"):
                stack_trace = Auditor.get_stack_trace()
                stack_trace = [trace.replace("File \"", "")
                            .replace("\", line ", ":")
                            .replace(", in ", " in ") for trace in stack_trace]

                

            if log_output == 'log_console':
                
                # ANSI escape codes for different colors
                styles = {
                    'color_text_Black': "\033[30m",
                    'color_text_Red': "\033[31m",
                    'color_text_Green': "\033[32m",
                    'color_text_Yellow': "\033[33m",
                    'color_text_Blue': "\033[34m",
                    'color_text_Magenta': "\033[35m",
                    'color_text_Cyan': "\033[36m",
                    'color_text_White': "\033[37m",
                    'color_back_Black': "\033[40m",
                    'color_back_Red': "\033[41m",
                    'color_back_Green': "\033[42m",
                    'color_back_Yellow': "\033[43m",
                    'color_back_Blue': "\033[44m",
                    'color_back_Magenta': "\033[45m",
                    'color_back_Cyan': "\033[46m",
                    'color_back_White': "\033[47m",
                    'color_text_Bright_Black': "\033[90m",
                    'color_text_Bright_Red': "\033[91m",
                    'color_text_Bright_Green': "\033[92m",
                    'color_text_Bright_Yellow': "\033[93m",
                    'color_text_Bright_Blue': "\033[94m",
                    'color_text_Bright_Magenta': "\033[95m",
                    'color_text_Bright_Cyan': "\033[96m",
                    'color_text_Bright_White': "\033[97m",
                    'color_back_Bright_Black': "\033[100m",
                    'color_back_Bright_Red': "\033[101m",
                    'color_back_Bright_Green': "\033[102m",
                    'color_back_Bright_Yellow': "\033[103m",
                    'color_back_Bright_Blue': "\033[104m",
                    'color_back_Bright_Magenta': "\033[105m",
                    'color_back_Bright_Cyan': "\033[106m",
                    'color_back_Bright_White': "\033[107m",
                    'effect_Blink': "\033[5m",
                    'effect_Bold': "\033[1m",
                    'effect_Underline': "\033[4m",
                    'reset': "\033[0m",
                }
                style_in_use_flag = False
                for style in styles:
                    log_entry_enritched_new = log_entry_enritched.replace("<"+style+">", styles[style])
                    if log_entry_enritched_new != log_entry_enritched:
                        style_in_use_flag = True
                
                if style_in_use_flag == True:
                    log_entry_enritched += styles['reset']

                if(log_output_config['stack_trace'] == "true"):
                    log_entry_enritched += "\n".join(stack_trace)
                
                # write to console output
                print(log_entry_enritched)

            else:
                
                if(log_output_config['stack_trace'] == "true"):
                    log_entry_enritched += "\n".join(stack_trace)

                folder = os.sep.join([
                    log_files_location,
                    log_output_config['sub_folder']
                ])
                
                filename = "{}{}{}_{}{}".format(
                    folder,
                    os.sep,
                    base_file_path,
                    Auditor.get_timestamp(),
                    log_output_config['extension']
                )
                
                try:
                    os.makedirs(os.sep.join(filename.split(os.sep)[:-1]))
                except:
                    None

                text = "{}/n{}".format(log_entry_separator, log_entry_enritched)
                
                log_entry_enritched = open(filename, "a+", encoding='utf-8')
                log_entry_enritched.write(text)
                log_entry_enritched.close()
            
        except:
            None
    
    return None
    
    
    
def log_test_header(test_name):
    import re
    Auditor.set_test_name(test_name)
    test_name_text = test_name
    
    tickets = []
    matches = re.finditer('_C[0-9]+', test_name)
    for m in matches:
        ticket = m.group(0).replace("_", "")
        url = Auditor.config['tickets_url'] + ticket.replace("C", "")
        test_name_text = test_name_text.replace(ticket, "")
        tickets.append("["+ticket+"]("+url+")")
        
    
    log_text = ""
    log_text += "\n==========================================="
    log_text += "\n# TEST METHOD NAME:"
    log_text += "\n# {}".format(test_name)
    log_text += "\n-------------------------------------------"
    if tickets:
        log_text += "\n\nRelated tickets:\n"
        log_text += "\n".join(tickets) + "\n"

    log_text += "\n\n-------------------------------------------"
    log_text += "\nDate execution: {}\n".format(str(datetime.now()))
    log_text += "\n===========================================\n"
    
    log(log_text, mode="test")
    
    # DEBUG:
    # regex help:
    # find: (def\s.+:\n)\t\t
    # replace: $1\t\tlog(Auditor.get_filename_as_text() + " > " + Auditor.get_method_as_text())\n\t\t


def audit(mode):
    def decorator(function):
        def wrapper(*args, **kwargs):
            log_entry = Auditor.method_call_to_text(function.__name__, args, kwargs)
            
            log(log_entry, mode)
            
            result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator