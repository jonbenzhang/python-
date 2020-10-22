import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    # filename='./test.log',
                    filemode='a')
# import logging

logging.info("\033[1;29m this is color1 \033[0m")
logging.info("\033[1;30m this is color2 \033[0m")
logging.info("\033[1;31m this is color3 \033[0m")
logging.info("\033[1;32m this is color4 \033[0m")
logging.info("\033[1;33m this is color5 \033[0m")
logging.info("\033[1;34m this is color6 \033[0m")
logging.info("\033[1;35m this is color7 \033[0m")
logging.info("\033[1;36m this is color8 \033[0m")