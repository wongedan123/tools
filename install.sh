clear
echo "please wait process installing module  external from python :)"
sleep 2
apt-get update && upgrade
sleep 2
apt-get install python
sleep 2
apt-get install python2
sleep 2
pip2 install requirements
sleep 2
pip2 install html2text
sleep 2
pip2 install requests
sleep 2
pip2 install mechanize
clear
echo "installing finish please enter python2 tool.py"
echo ""
