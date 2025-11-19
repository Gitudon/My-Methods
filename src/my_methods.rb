def ping_to_ip(ip_address)
  require 'net/ping'
  pinger = Net::Ping::External.new(ip_address)
  if pinger.ping
    puts "#{ip_address} is reachable."
    true
  else
    puts "#{ip_address} is not reachable."
    false
  end
end