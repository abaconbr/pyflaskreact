#rm -rf ./server/static/
#mkdir ./server/static/
cd ./client/frontend
npm run build
cd ..
cd ..
export FLASK_APP=./server/app.py
flask run
