### Postmortem Report 🛠️💻

* * *

#### **Issue Summary:**

*   **Duration of outage:** 🚨 _30 minutes_ — from 10:00 AM to 10:30 AM UTC.
*   **Impact:** 🚫 _All users_ experienced downtime, unable to access the web service hosted by Nginx. (100% affected! 👎).
*   **Root cause:** 🤦‍♂️ A classic case of "wrong folder syndrome!" The Nginx configuration file was mistakenly pointing to the `sites-enabled` directory instead of `sites-available`. Oops! 🤷‍♀️

* * *

#### **Timeline:**

*   **10:00 AM UTC:** 🕵️‍♂️ _Detective Engineer_ notices "Connection Refused" while attempting to curl port 80. Immediate suspicion raised.
*   **10:05 AM UTC:** 🎯 Focus shifts to checking Nginx service and firewall settings (Spoiler alert: nothing wrong there!).
*   **10:10 AM UTC:** 🚪 Firewall's ruled out. Confusion mounts. An "Aha!" moment was still missing.
*   **10:15 AM UTC:** 🔍 Engineer discovers Nginx’s "Lost in Configuration" saga—`nginx.conf` was looking at the wrong folder.
*   **10:20 AM UTC:** 🏃‍♂️ Incident escalated to the _DevOps Avengers_ for further analysis.
*   **10:25 AM UTC:** 🔧 Problem fixed by modifying `nginx.conf` to point to `sites-available`, followed by restarting Nginx.
*   **10:30 AM UTC:** 🎉 Website back online! Port 80 is now _alive and kicking_, serving users again.

* * *

#### **Root Cause and Resolution:**

##### **What went wrong?** 🧐

The `nginx.conf` was referencing the `sites-enabled` directory, but the configuration files were sitting comfortably in `sites-available`, sipping coffee and waiting to be used. Since Nginx couldn’t find the correct config, it decided not to serve content at all—typical Nginx tantrum. 🙃

##### **How we fixed it:** 🛠️

*   Step 1: Updated the `nginx.conf` file to reference the right directory (`sites-available`).
*   Step 2: Gave Nginx a fresh start with a restart. (That’s the IT equivalent of "turn it off and back on again").
*   Step 3: Verified that Nginx is listening on port 80, and voilà—the site was back up!

* * *

#### **Corrective and Preventative Measures:**

**Lessons learned:** 🎓

*   Don’t trust Nginx’s sense of direction. It sometimes needs a bit of help finding the right folder.

* * *

#### **Improvements moving forward:**

1.  **Pre-Deployment Checklist:** ✅ Ensure `nginx.conf` is pointing in the right direction before it gets deployed.
    
2.  **Automated Monitoring:** 🕵️‍♀️ Have bots run around checking that Nginx is serving content and not lazing around with “Connection Refused” messages.
    
3.  **Nginx Alerts:** 🚨 Early warning systems to scream at us if Nginx isn't responding on port 80.
    

* * *

#### **Visual Summary (For the meme lovers)** 🎨

* * *

#### **Task List:**

*    Create a config validation script to avoid future misadventures.
*    Set up automated tests that ping port 80 and ensure Nginx isn’t on a coffee break.
*    Implement alerts that notify us before users even notice something’s wrong.

* * *

_And remember folks: in the land of servers, always check your folders—because even Nginx gets lost sometimes!_ 😉
