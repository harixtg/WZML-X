#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'Repo'
    ST_BN1_URL = 'https://www.github.com/weebzone/WZML-X'
    ST_BN2_NAME = 'Updates'
    ST_BN2_URL = 'https://t.me/WZML_X'
    ST_MSG = '''<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ Activated ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log Display'
    WEB_PASTE_BT = '📨 Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'Basic'
    USER_BT = 'Users'
    MICS_BT = 'Mics'
    O_S_BT = 'Owner & Sudos'
    CLOSE_BT = 'Close'
    HELP_HEADER = "㊂ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''<b>𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗜𝗦𝗧𝗜𝗖𝗦</b>

<b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :</b> {bot_uptime}

<b>ʀᴀᴍ - ᴍᴇᴍᴏʀʏ :</b>
{ram_bar} {ram}%
<b>ᴜ :</b> {ram_u} | <b>ғ :</b> {ram_f} | <b>ᴛ :</b> {ram_t}

<b>sᴡᴀᴘ - ᴍᴇᴍᴏʀʏ :</b>
{swap_bar} {swap}%
<b>ᴜ :</b> {swap_u} | <b>ғ :</b> {swap_f} | <b>ᴛ :</b> {swap_t}

<b>ᴅɪsᴋ :</b>
{disk_bar} {disk}%
<b>ᴛᴏᴛᴀʟ ᴅɪsᴋ ʀᴇᴀᴅ :</b> {disk_read}
<b>ᴛᴏᴛᴀʟ ᴅɪsᴋ ᴡʀɪᴛᴇ :</b> {disk_write}
<b>ᴜ :</b> {disk_u} | <b>ғ :</b> {disk_f} | <b>ᴛ :</b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ <b><i>NETWORK STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>BOT LIMITATIONS :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>Restarting...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}'''
    RESTARTED = '''⌬ <b><i>Bot Restarted!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>Starting Ping..</i>'
    PING_VALUE = '<b>Pong</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START =           "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b>✓ ɴᴀᴍᴇ : <code>{Name}</code></b>\n\n'
    SIZE =                  '<b>┌  sɪᴢᴇ : </b><code>{Size}</code>\n'
    ELAPSE =                '<b>├  ᴇʟᴀᴘsᴇᴅ : </b><code>{Time}</code>\n'
    MODE =                  '<b>├  ᴍᴏᴅᴇ : </b><code>{Mode}</code>\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '<b>├ ᴛᴏᴛᴀʟ ғɪʟᴇs : </b><code>{Files}</code>\n'
    L_CORRUPTED_FILES =     '<b>├ ᴄᴏʀʀᴜᴘᴛᴇᴅ ғɪʟᴇs : </b><code>{Corrupt}</code>\n'
    L_CC =                  '<b>└ ᴜᴘʟᴏᴅᴇ ʙʏ: </b><code>{Tag}</code>\n\n'
    PM_BOT_MSG =            '<b>🔰 ғɪʟᴇ ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴀʙᴏᴠᴇ...</b>'
    L_BOT_MSG =             '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ ᴘʀɪᴠᴀᴛᴇ...</b>'
    L_LL_MSG =              '<b>🔰 ғɪʟᴇ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇꜱꜱ ᴠɪᴀ ʟɪɴᴋꜱ...</b>\n'

    # ----- MIRROR -------
    M_TYPE =                '<b>├  ᴛʏᴘᴇ : </b><code>{Mimetype}</code>\n'
    M_SUBFOLD =             '<b>├  sᴜʙғᴏʟᴅᴇʀs : </b><code>{Folder}</code>\n'
    TOTAL_FILES =           '<b>├  ғɪʟᴇs : </b><code>{Files}</code>\n'
    RCPATH =                '<b>├  ᴘᴀᴛʜ : </b><code>{RCpath}</code>\n'
    M_CC =                  '<b>└  ᴜᴘʟᴏᴅᴇ : </b>{Tag}\n\n'
    M_BOT_MSG =             '<b>🔰 ʟɪɴᴋ (ꜱ) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ ᴘʀɪᴠᴀᴛᴇ</b>'

    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ ᴄʟᴏᴜᴅ ʟɪɴᴋ'
    SAVE_MSG =        '📨 sᴀᴠᴇ ᴍᴇᴇssᴀɢᴇ'
    RCLONE_LINK =     '♻️ ʀᴄʟᴏɴᴇ ʟɪɴᴋ'
    DDL_LINK =        '📎 {Serv} ʟɪɴᴋ'
    SOURCE_URL =      '🔐 sᴏᴜʀᴄᴇ ʟɪɴᴋ'
    INDEX_LINK_F =    '🗂 ɪɴᴅᴇx ʟɪɴᴋ'
    INDEX_LINK_D =    '⚡ ɪɴᴅᴇx ʟɪɴᴋ'
    VIEW_LINK =       '🌐 ᴠɪᴇᴡ ʟɪɴᴋ'
    CHECK_PM =        '❗ ᴠɪᴇᴡ ɪɴ ʙᴏᴛ ᴘᴍ ❗'
    CHECK_LL =        '🖇 ᴠɪᴇᴡ ɪɴ ʟɪɴᴋ ʟᴏɢ'
    MEDIAINFO_LINK =  '📃 ᴍᴇᴅɪᴀ ɪɴғᴏ'
    SCREENSHOTS =     '🖼 ScreenShots'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b>✓ ғɪʟᴇ ɴᴀᴍᴇ :</b> <code>{Name}</code>\n'

    #####---------PROGRESSIVE STATUS-------
    OMG =               '\n<b>┌────❪ ᴏᴍɢ × ᴄʟᴏᴜᴅ ❫─────༻</b>'
    BAR =               '\n<b>├  {Bar}</b>'
    PROCESSED =         '\n<b>├  ᴘʀᴏᴄᴇssᴇᴅ :</b> <code>{Processed}</code>'
    STATUS =            '\n<b>├  sᴛᴀᴛᴜs  :</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ᴇᴛᴀ :</b> <code>{Eta}</code>'
    SPEED =             '\n<b>├  sᴘᴇᴇᴅ  :</b> <code>{Speed}</code>'
    ELAPSED =                                     ' | <b>ᴇʟᴀᴘsᴇᴅ :</b> <code>{Elapsed}</code>'
    ENGINE =            '\n<b>├  ᴇɴɢɪɴᴇ  :</b> <code>{Engine}</code>'
    STA_MODE =          '\n<b>├  ᴍᴏᴅᴇ  :</b> <code>{Mode}</code>'
    SEEDERS =           '\n<b>├  sᴇᴇᴅᴇʀs  :</b> <code>{Seeders}</code> | '
    LEECHERS =                                           '<b>ʟᴇᴇᴄʜᴇʀs  :</b> <code>{Leechers}</code>'

    ####--------SEEDING----------
    SEED_SIZE =      '\n<b>├  sɪᴢᴇ  : </b><code>{Size}</code>'
    SEED_SPEED =     '\n<b>├  sᴘᴇᴇᴅ  : </b><code>{Speed}</code> | '
    UPLOADED =                                     '<b>ᴜᴘʟᴏᴀᴅᴇᴅ : </b><code>{Upload}</code>'
    RATIO =          '\n<b>├  ʀᴀᴛɪᴏ  : </b><code>{Ratio}</code> | '
    TIME =                                         '<b>ᴛɪᴍᴇ : </b><code>{Time}</code>'
    SEED_ENGINE =    '\n<b>├  ᴇɴɢɪɴᴇ  : </b><code>{Engine}</code>'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n<b>├  sɪᴢᴇ  : </b><code>{Size}</code>'
    NON_ENGINE =     '\n<b>├  ᴇɴɢɪɴᴇ  : </b><code>{Engine}</code>'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n<b>├  ᴜsᴇʀ  : </b><code>{User}</code> | '
    ID =                                                        '<b>ɪᴅ :</b> <code>{Id}</code>'
    BTSEL =          '\n<b>├  sᴇʟᴇᴄᴛ  : </b><code>{Btsel}</code>'
    CANCEL =         '\n<b>└  ᴄᴀɴᴄʟᴇ  : </b><code>{Cancel}</code>\n\n'

    ####------FOOTER--------
    FOOTER =          '<b>┌────❪ ʙᴏᴛ sᴛᴀᴛᴜs ❫─────༻</b>\n'
    TASKS =           '<b>├  ᴛᴀsᴋs :</b> <code>{Tasks}</code>\n'
    BOT_TASKS =       '<b>├  ᴛᴀsᴋs :</b> <code>{Tasks}/{Ttask}</code> | <b>ᴀᴠʟ :</b> <code>{Free}</code>\n'
    Cpu =             '<b>├  ᴄᴘᴜ :</b> <code>{cpu}% | '
    FREE =                                   '<b>ғʀᴇᴇ :</b> <code>{free} [{free_p}%]</code>\n'
    Ram =             '<b>├  ʀᴀᴍ :</b> <code>{ram}%</code> | '
    uptime =                                 '<b>ᴜᴘᴛɪᴍᴇ :</b> <code>{uptime}</code>\n'
    DL =              '<b>├  ᴅʟ :</b> <code>{DL}/s</code> | '
    UL =                                      '<b>ᴜʟ :</b> <code>{UL}/s</code>\n'
    HK =              '<b>└──────────────────༻</b>'

    ###--------BUTTONS-------
    PREVIOUS = '⇇ ʙᴀᴄᴋ'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = 'ɴᴇxᴛ ⇉'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'File/Folder is already available in Drive.\nHere are {content} list results:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>Counting:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>Size: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>Type: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>SubFolders: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>Files: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>By: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>Searching for <i>{NAME}</i></b>'
    LIST_FOUND = '<b>Found {NO} result for <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'No result found for <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}

➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day'''

    LEECH = '''㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>'''
