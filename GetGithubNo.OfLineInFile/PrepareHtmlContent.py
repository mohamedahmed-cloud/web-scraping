htmlContent = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="Assests/GitHub-logo1.png">
    <link rel="stylesheet" href="style.css">
    <title>Result</title>
</head>
<body>
<div class='contain'> <h2 class = 'Our_Learder'> صلى على الحبيب </h2>  </div>
'''


def data(allData):
    global htmlContent
    for arr in allData:
        for userName, content in arr.items():
            print(userName,content)
            cnt = 1
            htmlContent += "<div class= 'container'>"
            htmlContent += f"<details> <summary>{userName} </summary>"
            htmlContent += """
                <table>
                    <tr class='header'> 
                        <td> File Path</td> 
                        <td> No. Of Line In File.</td>
                    </tr>
            """

            for i in content:
                if cnt % 2 == 0:
                    htmlContent += "<tr class = 'one'>"
                else:
                    htmlContent += "<tr class = 'two'>"
                cnt += 1
                
                htmlContent += f"<td class = 'file'> {i[0]} </td>\n"
                htmlContent += f"<td class = 'line-number'>{i[1]}</td>\n"
                htmlContent += '</tr>\n'
        
            htmlContent += "</table>\n </details> \n </div>\n"
            htmlContent += "</body>\n "
    return htmlContent

