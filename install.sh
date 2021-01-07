echo -e "
 ▀▀█▀▀ ░█─░█ ▀█▀ ░█▀▀█ ░█▀▀▄ 　 ░█▀▀▀ ░█──░█ ░█▀▀▀ 
 ─░█── ░█▀▀█ ░█─ ░█▄▄▀ ░█─░█ 　 ░█▀▀▀ ░█▄▄▄█ ░█▀▀▀ 
 ─░█── ░█─░█ ▄█▄ ░█─░█ ░█▄▄▀ 　 ░█▄▄▄ ──░█── ░█▄▄▄        v1.0
						   Coded By H1mzy0t1 :)"

echo  "INSTALLING THIRDEYE.....";
echo  "Installing Requirments.....";
sudo apt-get update
sudo apt install python3-pip -y
sudo pip install colorama
sudo pip install requests
echo  "[/] Creating Link ...";
echo  "#!/bin/bash
python3 /usr/share/thirdeye/thirdeye.py" '${1+"$@"}' > "thirdeye";
chmod +x "thirdeye";
sudo mkdir "/usr/share/thirdeye"
sudo cp "install.sh" "/usr/share/thirdeye"
sudo cp "update.sh" "/usr/share/thirdeye"
sudo chmod +x /usr/share/thirdeye/update.sh
sudo cp "thirdeye.py" "/usr/share/thirdeye"
sudo cp "thirdeye" "/usr/local/bin/"
rm "thirdeye";
echo  "Yayy!! Successfully Installed ";
echo  "And Will Start In 3s.......";
echo  "You can also execute the tool by typing thirdeye";
sleep 3;
thirdeye
