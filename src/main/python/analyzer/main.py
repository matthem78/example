import logging                                                                       
                                                                                     
def get_console_logger(logger_name, log_level):                                      
    logger = logging.getLogger(logger_name)                                          
    logger.setLevel(log_level)                                                       
                                                                                     
    # create console handler and set level to debug                                  
    console = logging.StreamHandler()                                                
    console.setLevel(log_level)                                                      
                                                                                     
    # create formatter                                                               
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                                                                                     
    # add formatter to ch                                                            
    console.setFormatter(formatter)                                                  
                                                                                     
    # add console handlger to logger                                                 
    if not logger.handlers:                                                          
        logger.addHandler(console)                                                   
                                                                                     
    return logger         

LOGGER = get_console_logger('analyzer.main', logging.DEBUG)
LOGGER.info('test')
