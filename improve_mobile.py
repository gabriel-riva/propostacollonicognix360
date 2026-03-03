#!/usr/bin/env python3
"""
Improve Colloni portal mobile experience.
- Enhanced mobile media queries
- Mobile bottom navigation bar
- Better font sizes, scrolling, and layout for small screens
"""
import re

INPUT_FILE = 'proposta-colloni-slides.html'

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. REPLACE the existing @media(max-width:700px) block with
#    a comprehensive mobile-friendly version
# ============================================================
OLD_700 = (
    '@media(max-width:700px){'
    '.cards-3{grid-template-columns:1fr}'
    '.method-grid{grid-template-columns:1fr}'
    '.pricing-grid{grid-template-columns:1fr}'
    '.inc-grid{grid-template-columns:1fr}'
    '.portal-ui{grid-template-columns:1fr}'
    '.portal-sidebar{display:none}'
    '.portal-cards{grid-template-columns:1fr}'
    '.portal-row{grid-template-columns:1fr}'
    '#nav-dots{display:none}}'
)

NEW_MOBILE_CSS = """@media(max-width:700px){
.cards-3{grid-template-columns:1fr}
.method-grid{grid-template-columns:1fr}
.pricing-grid{grid-template-columns:1fr}
.inc-grid{grid-template-columns:1fr}
#nav-dots{display:none}

/* === PORTAL MOBILE LAYOUT === */
.portal-ui{
  grid-template-columns:1fr;
  aspect-ratio:auto;
  max-height:70vh;
  overflow:visible;
  border-radius:12px;
  position:relative;
}
.portal-sidebar{display:none}
.portal-main{
  overflow-y:auto;
  overflow-x:hidden;
  -webkit-overflow-scrolling:touch;
  height:auto;
  max-height:calc(70vh - 48px);
  padding:0.8rem 0.7rem 0.5rem;
  padding-bottom:56px;
}

/* Mobile bottom nav */
.portal-mobile-nav{
  display:flex;
  justify-content:space-around;
  align-items:center;
  background:linear-gradient(180deg,#3D2508 0%,#2C1A05 100%);
  padding:6px 0 max(6px,env(safe-area-inset-bottom));
  position:absolute;
  bottom:0;
  left:0;
  right:0;
  z-index:10;
  border-radius:0 0 12px 12px;
  box-shadow:0 -2px 8px rgba(0,0,0,0.15);
}
.portal-mobile-nav-item{
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:2px;
  color:rgba(224,213,192,0.6);
  font-size:0.55rem;
  font-family:var(--font-body);
  padding:4px 6px;
  border-radius:6px;
  cursor:pointer;
  transition:color 0.2s,background 0.2s;
  user-select:none;
  -webkit-tap-highlight-color:transparent;
  min-width:0;
  flex:1;
  text-align:center;
}
.portal-mobile-nav-item .mob-icon{
  font-size:1rem;
  line-height:1;
}
.portal-mobile-nav-item .mob-label{
  font-size:0.5rem;
  white-space:nowrap;
  overflow:hidden;
  text-overflow:ellipsis;
  max-width:56px;
}
.portal-mobile-nav-item.active{
  color:#FFF;
  background:rgba(255,255,255,0.12);
}

/* Portal header mobile */
.portal-header{
  margin-bottom:0.6rem;
}
.portal-greeting{
  font-size:0.85rem;
}
.portal-avatar{
  width:28px;height:28px;
  font-size:0.6rem;
}

/* Stat cards: 2 columns on mobile */
.portal-cards{
  grid-template-columns:repeat(2,1fr);
  gap:0.4rem;
  margin-bottom:0.6rem;
}
.portal-stat-card{
  padding:0.5rem;
}
.portal-stat-card .portal-box-title,
.portal-stat-card div[style*="font-size"]{
  font-size:0.6rem !important;
}

/* Portal rows single column */
.portal-row{grid-template-columns:1fr}
.portal-box{padding:0.6rem}
.portal-box-title{font-size:0.7rem}

/* === EAD / TRILHAS MOBILE === */
.ead-search input{
  font-size:0.75rem;
  padding:0.5rem;
}
.ead-trails{
  grid-template-columns:1fr;
  gap:0.5rem;
}
.ead-trail-card{
  display:grid;
  grid-template-columns:auto 1fr;
}
.ead-trail-header{
  padding:0.5rem;
  border-radius:10px 0 0 10px;
  min-width:80px;
  display:flex;
  flex-direction:column;
  justify-content:center;
}
.ead-trail-body{
  padding:0.5rem;
  display:flex;
  flex-direction:column;
  justify-content:center;
}
.ead-trail-title{font-size:0.7rem}
.ead-trail-sub{font-size:0.55rem}
.ead-trail-badge{font-size:0.5rem}
.ead-trail-meta{font-size:0.55rem}

/* EAD Videos: 1 column */
.ead-videos{
  grid-template-columns:1fr;
  gap:0.5rem;
}
.ead-video-card{
  display:grid;
  grid-template-columns:80px 1fr;
}
.ead-video-thumb{
  height:100%;
  min-height:44px;
  border-radius:8px 0 0 8px;
}
.ead-video-info{padding:0.4rem 0.5rem}
.ead-video-title{font-size:0.65rem}
.ead-video-meta{font-size:0.5rem}

/* === COMMUNITY MOBILE === */
.community-feed{gap:0.4rem}
.community-post{padding:0.6rem}
.community-post-avatar{width:24px;height:24px;font-size:0.5rem}
.community-post-name{font-size:0.7rem}
.community-post-time{font-size:0.5rem}
.community-post-text{font-size:0.65rem;line-height:1.4}
.community-post-actions{font-size:0.55rem;gap:0.8rem}
.community-champs{gap:0.3rem}
.community-champ{font-size:0.55rem;padding:0.2rem 0.4rem}

/* === KANBAN MOBILE: horizontal scroll === */
.kanban{
  grid-template-columns:repeat(3,minmax(200px,1fr));
  gap:0.4rem;
  overflow-x:auto;
  -webkit-overflow-scrolling:touch;
  scroll-snap-type:x mandatory;
  padding-bottom:4px;
}
.kanban-col{
  scroll-snap-align:center;
  min-width:200px;
}
.kanban-col-header{font-size:0.65rem}
.kanban-col-count{font-size:0.5rem}
.kanban-card{
  padding:0.4rem;
  font-size:0.6rem;
}
.kanban-card-title{font-size:0.65rem}
.kanban-card-tag{font-size:0.5rem}
.kanban-card-avatar{width:18px;height:18px;font-size:0.4rem}

/* === CALENDAR MOBILE === */
.cal-header{font-size:0.75rem;margin-bottom:0.3rem}
.cal-header-btn{font-size:0.6rem;padding:3px 8px}
.cal-day-label{font-size:0.5rem}
.cal-day{font-size:0.55rem;padding:4px 0}
.cal-events{gap:0.3rem}
.cal-event{
  padding:0.4rem;
  font-size:0.6rem;
}
.cal-event-date{font-size:0.6rem;min-width:30px}
.cal-event-time{font-size:0.5rem}

/* === DASHBOARD MOBILE === */
.dash-activity-item{font-size:0.6rem}
.dash-activity-time{font-size:0.5rem}
.dash-chart{height:40px}
.dash-quick-actions{
  flex-wrap:wrap;
  gap:0.3rem;
}
.dash-quick-btn{
  flex:1 1 calc(50% - 0.15rem);
  min-width:0;
  padding:0.4rem;
  font-size:0.55rem;
}

/* Projects mobile */
.portal-proj-name{font-size:0.65rem}
.portal-proj-status{font-size:0.5rem}
.portal-proj-meta{font-size:0.55rem}
.portal-proj-bar{height:5px}

/* General mobile typography */
.portal-meeting-date{font-size:0.55rem}
.portal-meeting-item{font-size:0.6rem}
.portal-task-text{font-size:0.65rem}
.portal-task-check{width:16px;height:16px}
.portal-lib-item{font-size:0.65rem}
.portal-champ-item{font-size:0.6rem}
.portal-champ-avatar{width:26px;height:26px;font-size:0.55rem}
.portal-champ-badge{font-size:0.5rem}
.portal-interactive-hint{font-size:0.55rem;padding:0.25rem 0.6rem}
}

/* Extra small screens */
@media(max-width:480px){
.portal-ui{max-height:75vh}
.portal-main{max-height:calc(75vh - 48px)}
.portal-cards{grid-template-columns:1fr}
.kanban{grid-template-columns:repeat(3,minmax(180px,1fr))}
.kanban-col{min-width:180px}
.ead-trail-card{grid-template-columns:1fr}
.ead-trail-header{border-radius:10px 10px 0 0;min-width:auto}
.ead-video-card{grid-template-columns:1fr}
.ead-video-thumb{border-radius:8px 8px 0 0;height:48px;min-height:48px}
.dash-quick-btn{flex:1 1 100%}
}"""

# Remove newlines for minified injection
NEW_MOBILE_MINIFIED = re.sub(r'\n\s*', '', NEW_MOBILE_CSS)
# But keep the comment markers for readability in source
NEW_MOBILE_MINIFIED = re.sub(r'/\*[^*]*\*/', '', NEW_MOBILE_MINIFIED)

html = html.replace(OLD_700, NEW_MOBILE_MINIFIED)

# ============================================================
# 2. ADD mobile bottom navigation HTML right before portal-ui
#    closing div. We find the right spot by looking for the
#    portal's JavaScript init code reference.
# ============================================================

# The mobile nav needs to be inside .portal-ui but after .portal-main
# Find the closing of portal-main and before closing of portal-ui
# Strategy: find the pattern where portal-main's views end and
# the portal-ui div closes

MOBILE_NAV_HTML = (
    '<div class="portal-mobile-nav">'
    '<div class="portal-mobile-nav-item active" data-view="dashboard">'
    '<span class="mob-icon">&#9776;</span>'
    '<span class="mob-label">Início</span></div>'
    '<div class="portal-mobile-nav-item" data-view="trilhas">'
    '<span class="mob-icon">&#9733;</span>'
    '<span class="mob-label">Trilhas</span></div>'
    '<div class="portal-mobile-nav-item" data-view="comunidade">'
    '<span class="mob-icon">&#9825;</span>'
    '<span class="mob-label">Social</span></div>'
    '<div class="portal-mobile-nav-item" data-view="projetos">'
    '<span class="mob-icon">&#9881;</span>'
    '<span class="mob-label">Projetos</span></div>'
    '<div class="portal-mobile-nav-item" data-view="tarefas">'
    '<span class="mob-icon">&#9744;</span>'
    '<span class="mob-label">Tarefas</span></div>'
    '<div class="portal-mobile-nav-item" data-view="agenda">'
    '<span class="mob-icon">&#128197;</span>'
    '<span class="mob-label">Agenda</span></div>'
    '</div>'
)

# CSS to hide mobile nav on desktop (add before </style>)
MOBILE_NAV_CSS = '.portal-mobile-nav{display:none}'
style_close_pos = html.find('</style>')
if style_close_pos != -1:
    html = html[:style_close_pos] + MOBILE_NAV_CSS + html[style_close_pos:]

# Find the portal-main closing div sequence
# The portal-main section ends, then portal-ui closes
# We need to find the end of portal-main (which contains all the views)
# and insert the mobile nav between portal-main's closing and portal-ui's closing

# Strategy: Find the last portal-view div (agenda), then navigate to
# find where portal-ui closes

# Approach: find the string that marks the end of the portal section
# Looking for the "Investimento" section which comes after the portal
investimento_pos = html.find('Investimento')
if investimento_pos == -1:
    # Try alternative markers
    investimento_pos = html.find('investimento')

if investimento_pos != -1:
    # Go backwards from investimento to find the closing of portal-ui
    # The portal-ui is inside a slide div
    # Find the closest </div></div> before the next slide
    search_start = investimento_pos - 500
    search_area = html[search_start:investimento_pos]

    # Find the portal-ui container's end: it should be before the
    # investment slide. Look for a sequence of closing divs
    # before a new slide starts
    slide_before_invest = html.rfind('class="slide', 0, investimento_pos)
    if slide_before_invest != -1:
        # The portal-ui closing should be just before this slide
        # Find the div closing sequence before this slide
        portal_end_area = html[slide_before_invest - 200:slide_before_invest]
        print(f"Area before investment slide: ...{repr(portal_end_area[-100:])}")

# Alternative approach: find where portal-ui div ends using tag counting
portal_ui_start = html.find('class="portal-ui"')
if portal_ui_start != -1:
    # Navigate from portal-ui start, count opening/closing divs
    pos = html.rfind('<div', 0, portal_ui_start + 5)
    depth = 0
    i = pos
    while i < len(html):
        if html[i:i+4] == '<div':
            depth += 1
            i += 4
        elif html[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                # This is where portal-ui closes
                print(f"Portal-ui closes at position: {i}")
                # Insert mobile nav before this closing div
                html = html[:i] + MOBILE_NAV_HTML + html[i:]
                print("Mobile nav inserted!")
                break
            i += 6
        else:
            i += 1

# ============================================================
# 3. UPDATE the portal JavaScript to also handle mobile nav clicks
# ============================================================

# Find the initPortal function and add mobile nav support
OLD_INIT_PORTAL = "function initPortal(){"
NEW_INIT_PORTAL_EXTRA = """function initMobileNav(){
var mobItems=document.querySelectorAll('.portal-mobile-nav-item[data-view]');
var sideItems=document.querySelectorAll('.portal-nav-item[data-view]');
var views=document.querySelectorAll('.portal-view');
mobItems.forEach(function(item){
item.addEventListener('click',function(e){
e.stopPropagation();
var viewId='view-'+this.getAttribute('data-view');
mobItems.forEach(function(n){n.classList.remove('active')});
sideItems.forEach(function(n){n.classList.remove('active')});
views.forEach(function(v){v.classList.remove('active-view')});
this.classList.add('active');
sideItems.forEach(function(n){if(n.getAttribute('data-view')===item.getAttribute('data-view'))n.classList.add('active')});
var target=document.getElementById(viewId);
if(target){target.classList.add('active-view')}
else{document.getElementById('view-dashboard').classList.add('active-view')}
});
});
sideItems.forEach(function(item){
item.addEventListener('click',function(){
var dv=this.getAttribute('data-view');
mobItems.forEach(function(n){n.classList.remove('active')});
mobItems.forEach(function(n){if(n.getAttribute('data-view')===dv)n.classList.add('active')});
});
});
}
function initPortal(){"""

# Minify the JS
NEW_INIT_MINIFIED = re.sub(r'\n\s*', '', NEW_INIT_PORTAL_EXTRA)

html = html.replace(OLD_INIT_PORTAL, NEW_INIT_MINIFIED, 1)

# Also call initMobileNav after initPortal call
# Find where initPortal() is called
OLD_INIT_CALL = "initPortal();"
NEW_INIT_CALL = "initPortal();initMobileNav();"
html = html.replace(OLD_INIT_CALL, NEW_INIT_CALL, 1)

# ============================================================
# 4. WRITE the result
# ============================================================
with open(INPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

# Also update index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Mobile improvements applied.")
print(f"File size: {len(html)} bytes")
