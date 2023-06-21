from ReadUserNameLineFromCSV import ReadUserName
from get_All_User_Repos import Info
from SharableData import repoName
from collections import deque

fileredArray = deque()
allUserName = ReadUserName()
allUserRepo = Info()
def filterUser():
    for i, j in allUserRepo.items():
        if repoName in j.values():
            fileredArray.append(i)
    return fileredArray





'''
store = {'mohamedahmed-cloud': {0: 'Algorithm-From-Abdul-Bari', 1: 'Algorithms-and-Data-Structures-training---IEEE-CS-ZSB', 2: 'alx-low_level_programming', 3: 'alx-pre_course', 4: 'alx-system_engineering-devops', 5: 'alx-zero_day', 6: 'E-commerce-with-React', 7: 'Ecommerce-1', 8: 'Github-follower', 9: 'GitHub_File', 10: 'HackerranckJava', 11: 'HTML-CSS-Js-XO-project', 12: 'ICPC-Preparation', 13: 'IEEE-ZSB-Technical-Rookies-22', 14: 'Interrupt', 15: 'Iron-Man-Face', 16: 'Java-Work', 17: 'Linux-Module', 18: 'Math', 19: 'Node.js', 20: 'Parking-system', 21: 'Ping-pong-Using-Python', 22: 'printf', 23: 'React-Quiz-', 24: 'React-To-Do-Task', 25: 'RGB-Color', 26: 'Simple-Calculator-using-Python', 27: 'simple_shell', 28: 'Snake-Game', 29: 'Sql'}, 
        'MohamedHamed12345': {0: 'arduino_lab', 1: 'Data_analysis', 2: 'IEEE-ZSB-Technica1-Rookies-23', 3: 'IEEE_AI', 4: 'IEEE_proejct_1', 5: 'pronblems', 6: 'smart_roads', 7: 'sudoku_game'}, 
        'Abdelruhman2': {0: 'Abdelruhman2', 1: 'IEEE-Backend', 2: 'IEEE-ZSB-Technica1-Rookies-23', 3: 'Project'},
        'MuhammadSawalhy': {0: '3d-to-1d-matrix', 1: 'AI-IEEE-CS23-ZSB', 2: 'alif2', 3: 'alifstudio3', 4: 'api-design-node-v3', 5: 'bash-scripting', 6: 'bouncing-balls-javafx', 7: 'bugless', 8: 'canvas-lazy-update', 9: 'cheatsheets', 10: 'cv', 11: 'da7ee7-bot-dashboard', 12: 'da7ee7-civil-1st-year-telegram-bot', 13: 'edex-ui', 14: 'gauss-jordan-elimination', 15: 'i18n', 16: 'ICPC-Training-Level-1', 17: 'IEEE-ZSB-Technica1-Rookies-23', 18: 'IOT-NodeMCU', 19: 'js-ts-monorepos', 20: 'leanring-vb6', 21: 'learning-ml', 22: 'MuhammadSawalhy', 23: 'my-config', 24: 'note-taking', 25: 'notion-to-markdown', 26: 'problem-solving', 27: 'programming-in-embedded-systems-revealjs-presentation', 28: 'proleap-vb6-parser', 29: 'qt-function-plotter'}, 'ahmedsharaf19': {0: 'AI-IEEE--ZSB-S23', 1: 'Gauss-Jordan-Elimination', 2: 'IEEE-ZSB-Technica1-Rookies-23', 3: 'Sudoku-Game', 4: 'Words-Heap'},
        'jinroot': {0: 'freecodecamp-bash-course', 1: 'IEEE-backend', 2: 'IEEE-backend-1', 3: 'IEEE-ZSB-Technical-Rookies-23'}}
'''