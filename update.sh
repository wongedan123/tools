clear
echo ""
echo "please wait deleting old tools and installing new tools :)"
sleep 2
cd ../
sleep 1
rm -rf tools
git clone https://github.com/wongedan123/tools
sleep 2
clear
echo ""
echo "update finish :)"
sleep 2
clear
cd tools
echo " in tools wait 2 seccond"
sleep 2
python2 tool.py
