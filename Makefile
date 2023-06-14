all :
	echo "# web-scraping-" >> README.md
	git init
	git add *
	git commit -m "Finish get match Score and time from yalla kora"
	git branch -M main
	git remote add origin git@github.com:mohamedahmed-cloud/web-scraping-.git
	git push -u origin main