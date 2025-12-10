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


def gamma_function(n)
  if n <= 0
    raise ArgumentError, "Input must be a positive number."
  elsif n == 1
    1
  else
    (n - 1) * gamma_function(n - 1)
  end
end