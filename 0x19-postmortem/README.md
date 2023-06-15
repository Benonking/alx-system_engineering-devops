# Postmortem Reports
## Postmortem report for Mending minds server failure


![](https://github.com/Benonking/images/blob/main/system-failure-system-down.gif)
**Issued by**: Masereka Benon
**Position** : Backend Engineer

### Issue Summary
Between 10:30am and 11:45am users  experienced slow response to requests that one of the databases was not doing replication

The event was triggered by one of the web servers going down and therefore the load balancer was redirecting all client requests to one server

The issue was caused by a change in the web server configuration configuration file http block
The event was detected by datadog and the team started working on the problem by visiting the config file of web server 2 
Approximately 70% of all the active users were affected by this slow service.

### Timeline
10:30am – Issue detected by datadog
10:34am – Issue alert sent to development team
10:45am – Development team starts reviewing load balancer and server2 config file
11:13am – Took time to realize a junior developer had changed the server block in the config file without testing .The server was not listening on port 80
11.15am – Using version control, the server2 config file was restored to a previous stage
11:20am – testing of new changes and the sent to production

### Root cause and resolution
This issue caused 70% of all requests sent to the server to take twice as much response time as it took when all the servers were working properly.

The incident was caused by a junior developer who had been tasked to configure a new server for scaling and this new server was listening to a different port than the already established servers in production
This event caused the server to stop receiving and therefore not processing client requests. Hence leading to only one active server running
 
The development team up receiving a failure alert from a monitoring service had to restore the configuration to its previous using version control tools

Corrective and preventive measures
All server configurations will pass through thorough testing phase before being sent to production
