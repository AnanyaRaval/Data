import pandas as pd 

ifconfig = pd.DataFrame(columns = ['Command','NL Queries'])

ifconfig = ifconfig.append({'Command':'ifconfig','NL Queries':['Show all active interactive network interface details.',
											'How do I check link, hardware address, inetaddress, broadcast address etc. of all active network interfaces?',
											'How do I check which all active network hardware I have in my computer?']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 up','NL Queries':['Turn device eth0 up.',
																'Turn card eth0 up.',
																'How do I turn up my eth0 card?']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 172.16.25.125','NL Queries':['Make ip address of eth0 to be 172.16.25.125.',
																		'How do I assign ip address 172.16.25.125 to interface eth0?',
																		'Change ip address of eth0 = 172.16.25.125.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig -a','NL Queries':['Show all interactive network interface details.',
															'How do I check link, hardware address, inetaddress, broadcast address etc. of all network interfaces?',
															'Check the network hardware I have in my computer']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig enp2s0','NL Queries':['Show network interface details of enp2s0.',
										'How do I check link, hardware address, inetaddress, broadcast address etc. of enp2s0 interface.',
										'Display details of enp2s0 network interface only.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifup eth0','NL Queries':['Enable eth0 network interface.',
													'How do I make eth0 card active?',
													'Turn on eth0 card.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 down','NL Queries':['Turn down device eth0.',
															'Disable card eth0 down.',
															'How do I disable my eth0 card?']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifdown eth0','NL Queries':['Disable eth0 network interface.',	
																'How do I make eth0 card inactive?',
																'Turn off eth0 card.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig enp2s0 netmask 255.255.255.244','NL Queries':['Make netmask of enp2s0 as 255.255.255.224.',
																				'How do I assign network mask as 255.255.255.224 to interface enp2s0?',
																				'Change netmask address of enp2s0 = 255.255.255.224.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lxcbr0 broadcast 172.16.25.63','NL Queries':['Set broadcast address of lxcbr0 as 172.16.25.63.',	
																							'How do I assign broadcast address as 172.16.25.63 to interface lxcbr0?',
																							'Change broadcast address of lxcbr0 = 172.16.25.63.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig enp2s0 172.16.25.125 netmask 255.255.255.244 broadcast 172.16.25.63','NL Queries':['Make ip as 172.16.25.125 ,netmask as 255.255.255.244 ,broadcast address as 172.16.25.63 for the interface enp2s0.',
													'Assign ip,netmask,broadcast addresses as 172.16.25.125, 255.255.255.244, 172.16.25.63 to the interface enp2s0?',
													'Change ip => 172.16.25.125, netmask => 255.255.255.224, broadcast address => 172.16.25.63 of enp2s0.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lo mtu 1000','NL Queries':['Set the maximum transmission unit to lo interface to 1000 packets',
													'Assign mtu = 1000 packets for lo interface',
													'How to set mtu for lo interface?']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lxcbr0 promisc','NL Queries':['Enable promiscous mode for packet receiving to the network interface lxcbr0.',
															'How to allow all packets to pass through the network interface lxcbr0?',
															'Make lxcbr0 to not drop packets that don\'t belong to itself.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lxcbr0 -promisc','NL Queries':['Disable promiscous mode for packet receiving to the network interface lxcbr0.',
								'How to allow only packets that belong to lxcbr0 to pass through it?',
								'Make lxcbr0 to drop packets that don\'t belong to itself.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0:0 172.16.25.127','NL Queries':['Add an alias 172.16.25.125 to eth0 interface.',
							'How to insert an alias 172.16.25.125 to eth0?.',
							'Configure extra network interface to eth0 as 172.16.25.125.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0:0','NL Queries':['Check the alias to eth0 interface.',
										'How to check the alias to eth0?.',
										'What is the alias of eth0 interface?.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0:0 down','NL Queries':['Remove an alias to eth0 interface.',
										'How to remove an alias to eth0?.',
										'Delete an improperly configured alias to eth0 network interface.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 hw ether AA:BB:CC:DD:EE:FF','NL Queries':['Change MAC address of eth0 interface to AA:BB:CC:DD:EE:FF',
							'How to change media access control address of eth0 network interface to AA:BB:CC:DD:EE:FF.',
							'Modify the MAC address of eth0 => Aa:BB:CC:DD:EE:FF.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig -s','NL Queries':['Show all interactive network interface in a short list.',
								'List of all interface networks in short form.',
								'How do I check which active network hardware I have in my computer in short form?']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig -v','NL Queries':['Show all interactive network interface details in a verbose way.',
							'How do I check link, hardware address, inetaddress, broadcast address etc. of all active network interfaces with error messages?',
							'How do I check which network hardware I have in my computer in a verbose way?']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lxcbr0 arp','NL Queries':['Enable arp protocol to the network interface lxcbr0.',
						'How to allow ARP protocol for the network interface lxcbr0?',
						'Allow ARP protocol for the interface lxcbr0']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lxcbr0 -arp','NL Queries':['Disable arp protocol to the network interface lxcbr0.',
							'How to stop ARP protocol for the network interface lxcbr0?',
								'Make ARP protocol for the interface lxcbr0 disabled.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lo allmulti','NL Queries':['Enable all-multicast mode for packet receiving to the network interface lo.',
							'How to ensure all multicast packets to be recieved by the network interface lo?',
							'Make lo receive all multicast packets.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig lo -allmulti','NL Queries':['Disable all-multicast mode for packet receiving by the network interface lo.',
							'How to stop multicast packets to be recieved by the network interface lo?',
							'Stop lo receive multicast packets.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig wlan0 metric 1','NL Queries':['Set the interface metric as 1 for wlan0',
						'How to set interface metric as 1 for wlan0?',
						'For wlan0 network interface, set the metrci as 1.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig enp2s0 dstaddr 255.255.255.244','NL Queries':['Make destination address of enp2s0 as 255.255.255.224.',
							'How do I assign destination address as 255.255.255.224 to interface enp2s0?',
							'Change network destination address of enp2s0 = 255.255.255.224.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 add 2001:0db8:0:f101::1/64','NL Queries':['Add an IPv6 address 2001:0db8:0:f101::1/64 to eth0.',
								'How do I assign an IPv6 address as 2001:0db8:0:f101::1/64 to the interface eth0?',
								'Add IPv6 address to eth0 => 2001:0db8:0:f101::1/64.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 del 2001:0db8:0:f101::1/64','NL Queries':['Delete the IPv6 address 2001:0db8:0:f101::1/64 on eth0.',
								'How do I remove the IPv6 address 2001:0db8:0:f101::1/64 to the interface eth0?',
								'Delete IPv6 address to eth0 => 2001:0db8:0:f101::1/64.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig sit0 tunnel 172.16.254.1','NL Queries':['Add a tunneling address 172.16.254.1 to eth0.',
						'How do I assign a SIT address 172.16.254.1 to the interface sit0?',
						'Add SIT address to sit0 => 172.16.254.1.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 irq 15','NL Queries':['Set the interrupt line for eth0 as 15.',
																'How to change the interrupt line to 15 for the eth0 port?',
																'Change the IRQ setting to 15 for eth0.']},ignore_index=True)
#---
ifconfig = ifconfig.append({'Command':'ifconfig eth1 io_addr 172.16.254.1','NL Queries':['Set the start address as 172.16.254.1 in i/o space for eth1.',
										'How to set the start address as 172.16.254.1 for eth1?',
										'Make start address of eth1 i/o space = 172.16.254.1.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth1 mem_start 142.15.245.13','NL Queries':['Set the start address for shared memory as 142.15.245.13 for eth1.',
							'How to set the start address as 142.15.245.13 for shared memory used by eth1?',
							'Allocate a start address 142.15.245.13 for shared memory used by eth1.']},ignore_index=True)
#---

ifconfig = ifconfig.append({'Command':'ifconfig eth1 media 10base2','NL Queries':['Set the physical port to be used by eth1 as 10base2.',
										'How to set the medium type for eth1 as 10base2 ?',
										'Set the medium type for eth1 as thin ethernet.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth1 media auto','NL Queries':['Set the physical port to be used by eth1 automatically.',
												'How to set the medium type for eth1 automatically?',
												'Auto-detect the medium type for eth1.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 broadcast 123.25.22.1','NL Queries':['Set broadcast address 123.25.22.1 to eth0.',
										'How to add the broadcast address 123.25.22.1 to eth0?',
										'Assign broadcast address 123.25.22.1 to eth0 port.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 -broadcast 123.25.22.1','NL Queries':['Clear broadcast address 123.25.22.1 to eth0.',
												'How to remove the broadcast address 123.25.22.1 for eth0?',
												'Remove broadcast address 123.25.22.1 to eth0 port.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 pointopoint 123.25.22.1','NL Queries':['Set pointopoint address 123.25.22.1 to eth0.',
										'How to use point-to-point address 123.25.22.1 to eth0?',
										'Assign pointtopoint address 123.25.22.1 to eth0 port.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 -pointtopoint 123.25.22.1','NL Queries':['Clear pointopoint address 123.25.22.1 to eth0.',
									'How to remove the pointtopoint address 123.25.22.1 for eth0?',
									'Remove pointtopoint address 123.25.22.1 to eth0 port.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 hw class ether','NL Queries':['Set hardware address ether to eth0.',
							'How to set hardware class ether to eth0?',
							'Assign ether class to eth0 port.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth1 multicast','NL Queries':['Set the multicast flag for eth1 interface.',
								'How to set multicast flag for the the interface eth1?',
								'Turn on multicast flag for eth1 port.']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth1 address 192.168.27.100','NL Queries':['Set the IP address 192.168.27.100 to the port eth1.',
						'How to assign the IP address 192.168.27.100 to eth1 port?',
						'Assign eth1, the adress - 192.168.27.100 .']},ignore_index=True)

ifconfig = ifconfig.append({'Command':'ifconfig eth0 txqueuelen 5000','NL Queries':['Set the length of the transmit queue for eth0 as 5000.',
									'How to set the trasmit queue length 5000 for eth0?',
									'Change transmit queue length = 5000.']},ignore_index=True)

#ifconfig = ifconfig.append({'Command':'ifconfig ','NL Queries':['','','']},ignore_index=True)

print ifconfig.shape


