-- HEAD --

description = [[
A script that sees if a port is open.
]]

author = Jansen Lefever

-- RULE --

portrule = function(host, port)
        return port.protocol == "tcp"
                and port.state == "open"
end

-- ACTION --

action = function(host, port)
        return "This port is open!"
end
