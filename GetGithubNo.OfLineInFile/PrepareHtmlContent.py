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
<table>
'''

def data(allData):
    global htmlContent
    cnt = 1
    for i in allData:
        if cnt % 2 == 0:
            htmlContent += "<tr class = 'one'>"
        else:
            htmlContent += "<tr class = 'two'>"
        cnt += 1
        
        htmlContent += f"<td class = 'file'> {i[0]} </td>\n"
        htmlContent += f"<td class = 'line-number'>{i[1]}</td>\n"
        htmlContent += '</tr>\n'
  


    htmlContent += "</table>\n"
    htmlContent += "</body>\n"
    return htmlContent

