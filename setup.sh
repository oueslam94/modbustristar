echo INSTALLING PYTHON PACKAGES...
sudo pip3 install -r "requirements.txt";
echo LAUNCHING tristar-json.py...
python3 "tristar-json.py" &
echo LAUNCHING server.py...
python3 "server.py" &
cd "ReactApp/joesapp";
echo INSTALLING REACT PACKAGES...
sudo npm install;
echo STARTING UP ...
echo "

╔═══════════════════════════════╗
╠═════════════════════▄█════════╣
╠══════════════════▄██░█════════╣
╠═══════════█═════██░░░█════════╣
╠══════════██════██░░░░█════════╣
╠══════════█░█══▄█░░░░░█════════╣
╠═════════██░░█═█░░░░░░█════════╣
╠════════▄█░░░███░░░░░██════════╣
╠════════█░░░░█░░░░░░██████████▀╣
╠════════█░░░░░░░░░░░██░░░░░░██═╣
╠════════█░░░░▄▄▄▄▄░░░░░░░░░░█══╣
╠════════█░░▄▀░░░░░▀▄░░░░░░░█═══╣
╠═▀███████░▐░░░░░░░░░▌░░░░░█════╣
╠═══█░░░░░░▌░░░▄▄▄▄▄▄█▄░░░██════╣
╠═══██░░░░▐░░▄██████████▄░█═════╣
╠════█░░░░▌▄███████▀▀▀▀█▀█▀═════╣
╠════██░░▄▄████████░░░░▌░██═════╣
╠═════█▐██████▌███▌░░░░▐░░██════╣
╠══════██▌████▐██▐░░░░░▐░░░░██══╣
╠═════█▐█▐▌█▀███▀▀░░░░░▐░░░░░██═╣
╠════█░░██▐█░░▄░░░▄█░░░▐░░░░░░██╣
╠═══█░░░▐▌█▌▀▀░░░█░█▌░░▐░░░░████╣
╠══█░░░░▐▀▀░░░░▄█░░█▌░░▌░░███═══╣
╠▄██░░░░░▌░░░▄██░▄██▌░▐░███═════╣
╠═══██░░░▐░░▀█▄░▄███▌░▐░░█══════╣
╠════███░░█░░░██▀▀░█░░▌░░░█═════╣
╠══════█░░░▌░░▐█████░▐░░░░██════╣
╠═════█░░░░▐░░░░▀▀▀░░▌░░░░░█════╣
╠═════█░░░░░▀▄▄░░░░░█░░░░░░██═══╣
╠════██░░░░░░░░▀▄▄▄▀░░████████▄═╣
╠════█░░░░░█░░░░░░░░░░█═════════╣
╠════█░█████░░░░░█░░░░█═════════╣
╠════██════██░░░░██░░░█═════════╣
╠════█══════█░░░█═███░░█════════╣
╠═══════════█░░░█═══██░█════════╣
╠═══════════█░░░█═════██════════╣
╠═══════════██░░█══════█════════╣
╠════════════█░░█═══════════════╣
╠═════════════█░█═══════════════╣
╠══════════════██═══════════════╣
╚═══════════════════════════════╝
▒█▀▀▀█ █▀▀█ █░░ █▀▀█ █▀▀█ 　 ░░░▒█ █▀▀█ ░░░▒█ █▀▀█
░▀▀▀▄▄ █░░█ █░░ █▄▄█ █▄▄▀ 　 ░▄░▒█ █░░█ ░▄░▒█ █░░█
▒█▄▄▄█ ▀▀▀▀ ▀▀▀ ▀░░▀ ▀░▀▀ 　 ▒█▄▄█ ▀▀▀▀ ▒█▄▄█ ▀▀▀▀

"
sleep 2;
npm start;






# echo INSTALLING PYTHON PACKAGES...
# SLEEP 2
# pip install -r requirements.txt
# echo "SUCESS :)"
# SLEEP 2
# ./python.sh
# echo INSTALLING REACT PACKAGES...
# SLEEP 2
# cd ReactApp/joesapp
# # npm install
# echo "SUCESS :)"
# npm start
