# DDoS  
<b>Distributed Denial of Service</b>

Simple Python code for DDoS attack, <b>for education purposes only</b>. Implemented when I started learning about socket programming.  
  
This script can be used in a distributed manner, using servives or tools such MPI or Docker. Personally I did distributed-ly execute this script on 4 PC machines using MPI. The result is a really powerful website-killing weapon.
  
This code contain two version :  
  
<b>Socket version :</b> used Python socket library to send massive amount of request to the server.  
<b>Urllib2 version :</b> used Python urllib2 library to virtually visit the targeted website, increase hit counter of some weak web statistic services like <a target="_blank" href=http://www.histats.com/>Histat</a>.  
  
Proxy mode doesn't work yet.
