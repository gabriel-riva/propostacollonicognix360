"""
Complete Portal Colloni Mock Redesign
- Fixed height for all views
- Dashboard: modern stats with mini-charts, activity timeline
- Trilhas (was Biblioteca): EAD portal with course trails, videos
- Comunidade (was Champions): community feed, champion badges
- Projetos: modernized project cards
- Tarefas: Kanban board with 3 columns
- Agenda: Calendar grid + upcoming events
- Better sidebar colors, larger logo
"""
import re

with open('proposta-colloni-slides.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. CSS CHANGES
# ============================================================

# Fix portal-ui to FIXED height with 16:9 aspect ratio
html = html.replace(
    '.portal-ui{display:grid;grid-template-columns:clamp(140px,15vw,200px) 1fr;min-height:clamp(30vh,40vh,45vh)}',
    '.portal-ui{display:grid;grid-template-columns:clamp(140px,15vw,200px) 1fr;aspect-ratio:16/9;width:100%;max-height:clamp(38vh,46vh,54vh);overflow:hidden}'
)

# Better sidebar colors — warmer brown
html = html.replace(
    '.portal-sidebar{background:var(--colloni-primary);padding:clamp(0.5rem,1vh,1rem);color:#D4C8A8;font-size:clamp(0.6rem,0.8vw,0.75rem)}',
    '.portal-sidebar{background:linear-gradient(180deg,#3D2508 0%,#2C1A05 100%);padding:clamp(0.5rem,1vh,1rem);color:#E0D5C0;font-size:clamp(0.6rem,0.8vw,0.75rem);overflow:hidden}'
)

# Larger sidebar logo
html = html.replace(
    '.portal-sidebar-logo{padding:clamp(0.3rem,0.6vh,0.5rem) 0;margin-bottom:clamp(0.3rem,0.5vh,0.5rem);border-bottom:1px solid rgba(255,255,255,0.1)}',
    '.portal-sidebar-logo{padding:clamp(0.5rem,0.8vh,0.7rem) 0;margin-bottom:clamp(0.4rem,0.7vh,0.6rem);border-bottom:1px solid rgba(193,184,154,0.2)}.portal-sidebar-logo img{height:clamp(18px,2.5vh,26px)!important;filter:brightness(10)!important}'
)

# Portal main — hidden overflow for fixed height
html = html.replace(
    '.portal-main{padding:clamp(0.6rem,1.5vh,1.2rem);background:#FAFAFA;color:#1a1a1a}',
    '.portal-main{padding:clamp(0.6rem,1.5vh,1.2rem);background:#FAFAFA;color:#1a1a1a;overflow:hidden;height:100%}'
)

# Active nav item style — gold accent instead of white
if '.portal-nav-item:hover{background:rgba(255,255,255,0.1)}' in html:
    html = html.replace(
        '.portal-nav-item:hover{background:rgba(255,255,255,0.1)}',
        '.portal-nav-item:hover{background:rgba(193,184,154,0.12)}'
    )

# Better stat cards
html = html.replace(
    '.portal-stat-card{background:#FFF;border-radius:8px;padding:clamp(0.4rem,1vh,0.8rem);box-shadow:0 1px 3px rgba(0,0,0,0.06)}',
    '.portal-stat-card{background:#FFF;border-radius:10px;padding:clamp(0.4rem,1vh,0.8rem);box-shadow:0 1px 4px rgba(0,0,0,0.05);border:1px solid #F0EDE8}'
)

# Inject new CSS for EAD, Community, Kanban, Calendar
# Find position to inject — after the portal-interactive-hint rule
inject_marker = '@keyframes portalFadeIn'
inject_pos = html.find(inject_marker)
if inject_pos < 0:
    inject_marker = '.active-view{display:block}'
    inject_pos = html.find(inject_marker)

if inject_pos >= 0:
    end_of_marker = html.find('}', inject_pos) + 1

    new_css = """
.ead-search{margin-bottom:clamp(0.4rem,0.7vh,0.6rem)}
.ead-search input{width:100%;padding:clamp(0.25rem,0.5vh,0.4rem) clamp(0.4rem,0.8vw,0.6rem);border:1px solid #E5E7EB;border-radius:8px;font-size:clamp(0.5rem,0.7vw,0.65rem);background:#FFF;color:#374151;outline:none}
.ead-search input:focus{border-color:#C1B89A}
.ead-trails{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(0.3rem,0.6vw,0.5rem);margin-bottom:clamp(0.4rem,0.7vh,0.6rem)}
.ead-trail-card{border-radius:10px;overflow:hidden;background:#FFF;box-shadow:0 1px 4px rgba(0,0,0,0.06);border:1px solid #F0EDE8}
.ead-trail-header{padding:clamp(0.3rem,0.6vh,0.5rem) clamp(0.4rem,0.6vw,0.5rem);color:#FFF;position:relative}
.ead-trail-badge{font-size:clamp(0.35rem,0.45vw,0.45rem);background:rgba(255,255,255,0.2);padding:1px 5px;border-radius:100px;display:inline-block;margin-bottom:2px}
.ead-trail-title{font-size:clamp(0.55rem,0.7vw,0.68rem);font-weight:600;line-height:1.2}
.ead-trail-sub{font-size:clamp(0.4rem,0.5vw,0.5rem);opacity:0.8;margin-top:1px}
.ead-trail-body{padding:clamp(0.25rem,0.5vh,0.4rem) clamp(0.4rem,0.6vw,0.5rem)}
.ead-trail-bar{height:3px;background:#E5E7EB;border-radius:2px;overflow:hidden;margin-bottom:2px}
.ead-trail-fill{height:100%;border-radius:2px}
.ead-trail-meta{font-size:clamp(0.4rem,0.5vw,0.5rem);color:#9CA3AF;display:flex;justify-content:space-between}
.ead-videos{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(0.3rem,0.6vw,0.5rem)}
.ead-video-card{border-radius:8px;overflow:hidden;background:#FFF;box-shadow:0 1px 3px rgba(0,0,0,0.05);border:1px solid #F0EDE8}
.ead-video-thumb{height:clamp(28px,4vh,42px);display:flex;align-items:center;justify-content:center;font-size:clamp(0.7rem,1vw,0.9rem);color:#FFF;position:relative}
.ead-video-thumb::after{content:'';position:absolute;inset:0;background:rgba(0,0,0,0.2)}
.ead-video-info{padding:clamp(0.2rem,0.4vh,0.3rem) clamp(0.3rem,0.5vw,0.4rem)}
.ead-video-title{font-size:clamp(0.45rem,0.6vw,0.55rem);font-weight:500;color:#1a1a1a;line-height:1.2}
.ead-video-meta{font-size:clamp(0.35rem,0.45vw,0.45rem);color:#9CA3AF;margin-top:1px}
.community-feed{display:flex;flex-direction:column;gap:clamp(0.3rem,0.5vh,0.4rem);margin-bottom:clamp(0.4rem,0.7vh,0.6rem)}
.community-post{background:#FFF;border-radius:10px;padding:clamp(0.35rem,0.6vh,0.5rem) clamp(0.4rem,0.7vw,0.6rem);border:1px solid #F0EDE8}
.community-post-header{display:flex;align-items:center;gap:clamp(0.25rem,0.4vw,0.35rem);margin-bottom:clamp(0.15rem,0.3vh,0.25rem)}
.community-post-avatar{width:clamp(18px,2vh,24px);height:clamp(18px,2vh,24px);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#FFF;font-size:clamp(0.4rem,0.5vw,0.5rem);font-weight:700;flex-shrink:0}
.community-post-name{font-size:clamp(0.5rem,0.65vw,0.62rem);font-weight:600;color:#1a1a1a}
.community-post-time{font-size:clamp(0.35rem,0.45vw,0.45rem);color:#9CA3AF}
.community-post-text{font-size:clamp(0.45rem,0.6vw,0.58rem);color:#374151;line-height:1.3;margin-bottom:clamp(0.15rem,0.25vh,0.2rem)}
.community-post-actions{display:flex;gap:clamp(0.5rem,1vw,0.8rem);font-size:clamp(0.38rem,0.5vw,0.48rem);color:#9CA3AF}
.community-champs{display:flex;gap:clamp(0.3rem,0.5vw,0.4rem);flex-wrap:wrap}
.community-champ{display:flex;align-items:center;gap:clamp(0.2rem,0.3vw,0.25rem);background:#FFF;border-radius:100px;padding:clamp(0.15rem,0.25vh,0.2rem) clamp(0.3rem,0.5vw,0.4rem);border:1px solid #F0EDE8;font-size:clamp(0.4rem,0.55vw,0.52rem)}
.kanban{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(0.3rem,0.5vw,0.4rem);height:calc(100% - clamp(2rem,4vh,3.5rem))}
.kanban-col{background:#F3F2EE;border-radius:8px;padding:clamp(0.25rem,0.4vh,0.35rem) clamp(0.25rem,0.4vw,0.35rem);overflow:hidden}
.kanban-col-header{font-size:clamp(0.45rem,0.6vw,0.55rem);font-weight:600;color:#1a1a1a;margin-bottom:clamp(0.2rem,0.4vh,0.3rem);display:flex;align-items:center;gap:0.3rem}
.kanban-col-count{font-size:clamp(0.35rem,0.45vw,0.42rem);background:rgba(0,0,0,0.08);border-radius:100px;padding:0px 5px;font-weight:500}
.kanban-card{background:#FFF;border-radius:8px;padding:clamp(0.2rem,0.4vh,0.3rem) clamp(0.25rem,0.4vw,0.35rem);margin-bottom:clamp(0.15rem,0.3vh,0.25rem);box-shadow:0 1px 2px rgba(0,0,0,0.05);border:1px solid #E8E5DE;cursor:grab;font-size:clamp(0.42rem,0.55vw,0.52rem);transition:box-shadow 0.2s,transform 0.2s}
.kanban-card:hover{box-shadow:0 3px 8px rgba(0,0,0,0.1);transform:translateY(-1px)}
.kanban-card-title{font-weight:500;color:#1a1a1a;line-height:1.2;margin-bottom:2px}
.kanban-card-meta{display:flex;align-items:center;justify-content:space-between}
.kanban-card-tag{font-size:clamp(0.32rem,0.42vw,0.4rem);padding:1px 5px;border-radius:100px;font-weight:500}
.kanban-card-avatar{width:clamp(14px,1.8vh,18px);height:clamp(14px,1.8vh,18px);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#FFF;font-size:clamp(0.3rem,0.4vw,0.38rem);font-weight:700}
.cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:1px;margin-bottom:clamp(0.3rem,0.5vh,0.4rem)}
.cal-header{font-size:clamp(0.55rem,0.75vw,0.7rem);font-weight:600;color:#1a1a1a;display:flex;align-items:center;justify-content:space-between;margin-bottom:clamp(0.25rem,0.4vh,0.35rem)}
.cal-header-nav{display:flex;gap:clamp(0.3rem,0.5vw,0.4rem)}
.cal-header-btn{background:none;border:1px solid #E5E7EB;border-radius:6px;padding:1px 6px;font-size:clamp(0.4rem,0.55vw,0.5rem);color:#6B7280;cursor:pointer}
.cal-day-label{text-align:center;font-size:clamp(0.35rem,0.45vw,0.42rem);color:#9CA3AF;font-weight:500;padding:2px 0}
.cal-day{text-align:center;font-size:clamp(0.38rem,0.5vw,0.48rem);padding:clamp(2px,0.3vh,3px) 0;border-radius:6px;color:#374151;cursor:pointer}
.cal-day:hover{background:#F3F2EE}
.cal-day.today{background:#472D07;color:#FFF;font-weight:600}
.cal-day.has-event{position:relative}
.cal-day.has-event::after{content:'';position:absolute;bottom:1px;left:50%;transform:translateX(-50%);width:3px;height:3px;border-radius:50%;background:#C1B89A}
.cal-day.other-month{color:#D1D5DB}
.cal-events{display:flex;flex-direction:column;gap:clamp(0.15rem,0.25vh,0.2rem)}
.cal-event{display:flex;align-items:center;gap:clamp(0.25rem,0.4vw,0.35rem);padding:clamp(0.2rem,0.35vh,0.3rem) clamp(0.3rem,0.5vw,0.4rem);background:#FFF;border-radius:8px;border:1px solid #F0EDE8;font-size:clamp(0.42rem,0.55vw,0.52rem)}
.cal-event-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0}
.cal-event-date{font-weight:600;color:#472D07;min-width:clamp(24px,3vw,32px)}
.cal-event-title{color:#1a1a1a;font-weight:500}
.cal-event-time{color:#9CA3AF;font-size:clamp(0.35rem,0.45vw,0.42rem)}
.dash-activity{display:flex;flex-direction:column;gap:clamp(0.15rem,0.3vh,0.25rem)}
.dash-activity-item{display:flex;align-items:center;gap:clamp(0.25rem,0.4vw,0.35rem);font-size:clamp(0.42rem,0.55vw,0.52rem);color:#374151;padding:clamp(0.1rem,0.2vh,0.15rem) 0}
.dash-activity-dot{width:6px;height:6px;border-radius:50%;flex-shrink:0}
.dash-activity-time{font-size:clamp(0.35rem,0.45vw,0.42rem);color:#9CA3AF;margin-left:auto;white-space:nowrap}
.dash-chart{height:clamp(30px,5vh,50px);display:flex;align-items:flex-end;gap:2px;padding:clamp(0.2rem,0.3vh,0.25rem) 0}
.dash-chart-bar{flex:1;border-radius:2px 2px 0 0;transition:height 0.6s ease}
.dash-quick-actions{display:flex;gap:clamp(0.25rem,0.5vw,0.4rem)}
.dash-quick-btn{flex:1;padding:clamp(0.2rem,0.4vh,0.3rem);background:#FFF;border:1px solid #E8E5DE;border-radius:8px;text-align:center;font-size:clamp(0.4rem,0.55vw,0.5rem);color:#472D07;cursor:pointer;font-weight:500;transition:all 0.2s}
.dash-quick-btn:hover{border-color:#C1B89A;background:#FDFCF9}
""".replace('\n', '')

    html = html[:end_of_marker] + new_css + html[end_of_marker:]
    print('OK: Injected new CSS')

# ============================================================
# 2. SIDEBAR NAV CHANGES
# ============================================================

# Change "Biblioteca" to "Trilhas"
html = html.replace('data-view="biblioteca"', 'data-view="trilhas"')
html = html.replace(
    'stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>Biblioteca',
    'stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>Trilhas'
)

# Change "Champions" to "Comunidade"
html = html.replace('data-view="champions"', 'data-view="comunidade"')
html = html.replace(
    'stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>Champions',
    'stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>Comunidade'
)

# ============================================================
# 3. VIEW CONTENT REPLACEMENTS
# ============================================================

def find_view_content(html, view_id):
    """Find the inner content boundaries of a view div."""
    marker = f'id="{view_id}"'
    idx = html.find(marker)
    if idx < 0:
        return None, None
    # Find the > after the id attribute
    content_start = html.find('>', idx) + 1
    # Count div nesting to find the closing </div>
    pos = content_start
    depth = 1
    while depth > 0 and pos < len(html):
        next_open = html.find('<div', pos)
        next_close = html.find('</div>', pos)
        if next_close < 0:
            break
        if next_open >= 0 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            if depth == 0:
                return content_start, next_close
            pos = next_close + 6
    return None, None

def replace_view(html, view_id, new_content):
    start, end = find_view_content(html, view_id)
    if start and end:
        html = html[:start] + new_content + html[end:]
        print(f'OK: Replaced {view_id}')
    else:
        print(f'MISS: {view_id} not found')
    return html

# --- DASHBOARD ---
dashboard_html = (
    '<div class="portal-header"><div>'
    '<div class="portal-greeting">Bom dia, M&aacute;rcia</div>'
    '<div style="font-size:clamp(0.45rem,0.6vw,0.55rem);color:#9CA3AF">Colloni Participa&ccedil;&otilde;es</div>'
    '</div><div class="portal-avatar">MR</div></div>'
    # Stats row
    '<div class="portal-cards">'
    '<div class="portal-stat-card"><div style="display:flex;align-items:center;justify-content:space-between">'
    '<div><div class="stat-label">Horas</div><div class="stat-value">12<span style="font-size:0.65em;color:#9CA3AF">/16h</span></div></div>'
    '<div style="width:clamp(28px,3.5vw,38px);height:clamp(28px,3.5vw,38px);border-radius:50%;background:linear-gradient(135deg,#F0EDE8,#E8E2D6);display:flex;align-items:center;justify-content:center">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#472D07" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div></div></div>'
    '<div class="portal-stat-card"><div style="display:flex;align-items:center;justify-content:space-between">'
    '<div><div class="stat-label">Projetos</div><div class="stat-value" style="color:#3B82F6">5</div></div>'
    '<div style="width:clamp(28px,3.5vw,38px);height:clamp(28px,3.5vw,38px);border-radius:50%;background:linear-gradient(135deg,#EFF6FF,#DBEAFE);display:flex;align-items:center;justify-content:center">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#3B82F6" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 3v18"/></svg></div></div></div>'
    '<div class="portal-stat-card"><div style="display:flex;align-items:center;justify-content:space-between">'
    '<div><div class="stat-label">Champions</div><div class="stat-value" style="color:#22C55E">8</div></div>'
    '<div style="width:clamp(28px,3.5vw,38px);height:clamp(28px,3.5vw,38px);border-radius:50%;background:linear-gradient(135deg,#F0FDF4,#DCFCE7);display:flex;align-items:center;justify-content:center">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#22C55E" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div></div></div>'
    '</div>'
    # Mini chart + Activity
    '<div class="portal-row">'
    '<div class="portal-box"><div class="portal-box-title">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/></svg>'
    'Engajamento Semanal</div>'
    '<div class="dash-chart">'
    '<div class="dash-chart-bar" style="height:40%;background:#E8E2D6"></div>'
    '<div class="dash-chart-bar" style="height:65%;background:#E8E2D6"></div>'
    '<div class="dash-chart-bar" style="height:50%;background:#E8E2D6"></div>'
    '<div class="dash-chart-bar" style="height:80%;background:#C1B89A"></div>'
    '<div class="dash-chart-bar" style="height:70%;background:#C1B89A"></div>'
    '<div class="dash-chart-bar" style="height:90%;background:#472D07"></div>'
    '<div class="dash-chart-bar" style="height:75%;background:#472D07"></div>'
    '</div></div>'
    '<div class="portal-box"><div class="portal-box-title">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>'
    'Atividade Recente</div>'
    '<div class="dash-activity">'
    '<div class="dash-activity-item"><div class="dash-activity-dot" style="background:#22C55E"></div>Vin&iacute;cius completou trilha IA<div class="dash-activity-time">2h</div></div>'
    '<div class="dash-activity-item"><div class="dash-activity-dot" style="background:#3B82F6"></div>Novo projeto na Tecnotri<div class="dash-activity-time">5h</div></div>'
    '<div class="dash-activity-item"><div class="dash-activity-dot" style="background:#C1B89A"></div>Sess&atilde;o gravada dispon&iacute;vel<div class="dash-activity-time">1d</div></div>'
    '<div class="dash-activity-item"><div class="dash-activity-dot" style="background:#EAB308"></div>3 tarefas pendentes<div class="dash-activity-time">2d</div></div>'
    '</div></div></div>'
    # Quick actions
    '<div class="dash-quick-actions">'
    '<div class="dash-quick-btn">+ Nova Tarefa</div>'
    '<div class="dash-quick-btn">Agendar Sess&atilde;o</div>'
    '<div class="dash-quick-btn">Ver Trilhas</div>'
    '</div>'
)

# --- TRILHAS (EAD) ---
trilhas_html = (
    '<div class="portal-greeting">Trilhas de Aprendizado</div>'
    '<div class="ead-search"><input type="text" placeholder="Buscar cursos e materiais..."></div>'
    # Trail cards
    '<div class="ead-trails">'
    '<div class="ead-trail-card"><div class="ead-trail-header" style="background:linear-gradient(135deg,#472D07,#6B4E1E)">'
    '<div class="ead-trail-badge">4 m&oacute;dulos</div>'
    '<div class="ead-trail-title">Fundamentos de IA</div>'
    '<div class="ead-trail-sub">Para gestores</div>'
    '</div><div class="ead-trail-body">'
    '<div class="ead-trail-bar"><div class="ead-trail-fill" style="width:75%;background:#472D07"></div></div>'
    '<div class="ead-trail-meta"><span>75%</span><span>3/4</span></div></div></div>'
    '<div class="ead-trail-card"><div class="ead-trail-header" style="background:linear-gradient(135deg,#1E3A5F,#2563EB)">'
    '<div class="ead-trail-badge">6 m&oacute;dulos</div>'
    '<div class="ead-trail-title">Agentes Inteligentes</div>'
    '<div class="ead-trail-sub">Novo paradigma</div>'
    '</div><div class="ead-trail-body">'
    '<div class="ead-trail-bar"><div class="ead-trail-fill" style="width:33%;background:#2563EB"></div></div>'
    '<div class="ead-trail-meta"><span>33%</span><span>2/6</span></div></div></div>'
    '<div class="ead-trail-card"><div class="ead-trail-header" style="background:linear-gradient(135deg,#065F46,#059669)">'
    '<div class="ead-trail-badge">3 m&oacute;dulos</div>'
    '<div class="ead-trail-title">Automa&ccedil;&atilde;o Pr&aacute;tica</div>'
    '<div class="ead-trail-sub">Processos internos</div>'
    '</div><div class="ead-trail-body">'
    '<div class="ead-trail-bar"><div class="ead-trail-fill" style="width:0%;background:#059669"></div></div>'
    '<div class="ead-trail-meta"><span>Novo</span><span>0/3</span></div></div></div>'
    '</div>'
    # Recent videos
    '<div class="portal-box-title" style="margin-bottom:clamp(0.2rem,0.4vh,0.3rem)">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>'
    '&Uacute;ltimos V&iacute;deos</div>'
    '<div class="ead-videos">'
    '<div class="ead-video-card"><div class="ead-video-thumb" style="background:linear-gradient(135deg,#472D07,#8B6B3D)">'
    '<span style="position:relative;z-index:1">&#9654;</span></div>'
    '<div class="ead-video-info"><div class="ead-video-title">IA em Planilhas</div>'
    '<div class="ead-video-meta">12 min &middot; Fase 1</div></div></div>'
    '<div class="ead-video-card"><div class="ead-video-thumb" style="background:linear-gradient(135deg,#1E3A5F,#3B82F6)">'
    '<span style="position:relative;z-index:1">&#9654;</span></div>'
    '<div class="ead-video-info"><div class="ead-video-title">Agentes na Pr&aacute;tica</div>'
    '<div class="ead-video-meta">18 min &middot; Fase 2</div></div></div>'
    '<div class="ead-video-card"><div class="ead-video-thumb" style="background:linear-gradient(135deg,#065F46,#059669)">'
    '<span style="position:relative;z-index:1">&#9654;</span></div>'
    '<div class="ead-video-info"><div class="ead-video-title">Criando Solu&ccedil;&otilde;es</div>'
    '<div class="ead-video-meta">22 min &middot; Fase 2</div></div></div>'
    '</div>'
)

# --- COMUNIDADE ---
comunidade_html = (
    '<div class="portal-greeting">Comunidade Colloni</div>'
    '<div class="portal-cards">'
    '<div class="portal-stat-card"><div class="stat-label">Membros</div><div class="stat-value">23</div></div>'
    '<div class="portal-stat-card"><div class="stat-label">Posts esta semana</div><div class="stat-value" style="color:#3B82F6">7</div></div>'
    '<div class="portal-stat-card"><div class="stat-label">Champions Ativos</div><div class="stat-value" style="color:#22C55E">8</div></div>'
    '</div>'
    # Feed
    '<div class="community-feed">'
    '<div class="community-post"><div class="community-post-header">'
    '<div class="community-post-avatar" style="background:#3B82F6">VS</div>'
    '<div><div class="community-post-name">Vin&iacute;cius Segatt</div>'
    '<div class="community-post-time">h&aacute; 2 horas</div></div></div>'
    '<div class="community-post-text">Pessoal, testei o Claude para gerar relat&oacute;rios financeiros autom&aacute;ticos. Economizou 3h por semana no meu fluxo!</div>'
    '<div class="community-post-actions"><span style="color:#EF4444">&#9829; 5</span><span>&#128172; 3</span></div></div>'
    '<div class="community-post"><div class="community-post-header">'
    '<div class="community-post-avatar" style="background:#059669">RL</div>'
    '<div><div class="community-post-name">Rafaela Lopes</div>'
    '<div class="community-post-time">h&aacute; 5 horas &middot; Tecnotri</div></div></div>'
    '<div class="community-post-text">Compartilhando: criei um agente que monitora estoque de mat&eacute;ria-prima e avisa quando precisa repor. Super simples!</div>'
    '<div class="community-post-actions"><span style="color:#EF4444">&#9829; 8</span><span>&#128172; 6</span></div></div>'
    '<div class="community-post"><div class="community-post-header">'
    '<div class="community-post-avatar" style="background:#8B5CF6">MC</div>'
    '<div><div class="community-post-name">Marcos Caldeira</div>'
    '<div class="community-post-time">ontem &middot; Robustec</div></div></div>'
    '<div class="community-post-text">Algu&eacute;m j&aacute; conseguiu integrar IA com o ERP? Queria automatizar entrada de NFs.</div>'
    '<div class="community-post-actions"><span style="color:#EF4444">&#9829; 2</span><span>&#128172; 4</span></div></div>'
    '</div>'
    # Champions strip
    '<div class="portal-box-title" style="margin-bottom:clamp(0.15rem,0.3vh,0.2rem)">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
    'Champions</div>'
    '<div class="community-champs">'
    '<div class="community-champ"><div class="community-post-avatar" style="background:#3B82F6;width:16px;height:16px;font-size:0.35rem">VS</div>Vin&iacute;cius</div>'
    '<div class="community-champ"><div class="community-post-avatar" style="background:#059669;width:16px;height:16px;font-size:0.35rem">RL</div>Rafaela</div>'
    '<div class="community-champ"><div class="community-post-avatar" style="background:#EAB308;width:16px;height:16px;font-size:0.35rem">JP</div>Jo&atilde;o P.</div>'
    '<div class="community-champ"><div class="community-post-avatar" style="background:#8B5CF6;width:16px;height:16px;font-size:0.35rem">MC</div>Marcos</div>'
    '<div class="community-champ"><div class="community-post-avatar" style="background:#EC4899;width:16px;height:16px;font-size:0.35rem">AS</div>Ana S.</div>'
    '</div>'
)

# --- TAREFAS (KANBAN) ---
tarefas_html = (
    '<div class="portal-greeting">Quadro de Tarefas</div>'
    '<div class="kanban">'
    # Column 1: A Fazer
    '<div class="kanban-col"><div class="kanban-col-header"><div style="width:8px;height:8px;border-radius:50%;background:#EAB308"></div>A Fazer <span class="kanban-col-count">3</span></div>'
    '<div class="kanban-card"><div class="kanban-card-title">Identificar champion na Tecnotri</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#FEF3C7;color:#92400E">Fase 2</span>'
    '<div class="kanban-card-avatar" style="background:#3B82F6">VS</div></div></div>'
    '<div class="kanban-card"><div class="kanban-card-title">Mapear gargalo Robustec</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#DBEAFE;color:#1E40AF">An&aacute;lise</span>'
    '<div class="kanban-card-avatar" style="background:#059669">MR</div></div></div>'
    '<div class="kanban-card"><div class="kanban-card-title">Template de relat&oacute;rio IA</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#F3E8FF;color:#6B21A8">Material</span>'
    '<div class="kanban-card-avatar" style="background:#8B5CF6">GR</div></div></div>'
    '</div>'
    # Column 2: Em Andamento
    '<div class="kanban-col"><div class="kanban-col-header"><div style="width:8px;height:8px;border-radius:50%;background:#3B82F6"></div>Em Andamento <span class="kanban-col-count">2</span></div>'
    '<div class="kanban-card"><div class="kanban-card-title">Agente de estoque Tecnotri</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#DCFCE7;color:#166534">Projeto</span>'
    '<div class="kanban-card-avatar" style="background:#059669">RL</div></div></div>'
    '<div class="kanban-card"><div class="kanban-card-title">Treinamento gestores Movix</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#FEF3C7;color:#92400E">Fase 1</span>'
    '<div class="kanban-card-avatar" style="background:#EAB308">JP</div></div></div>'
    '</div>'
    # Column 3: Concluído
    '<div class="kanban-col"><div class="kanban-col-header"><div style="width:8px;height:8px;border-radius:50%;background:#22C55E"></div>Conclu&iacute;do <span class="kanban-col-count">3</span></div>'
    '<div class="kanban-card" style="opacity:0.7"><div class="kanban-card-title">Panorama IA apresentado</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#DCFCE7;color:#166534">Fase 1</span>'
    '<div class="kanban-card-avatar" style="background:#3B82F6">GR</div></div></div>'
    '<div class="kanban-card" style="opacity:0.7"><div class="kanban-card-title">Portal configurado</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#F3F4F6;color:#374151">Setup</span>'
    '<div class="kanban-card-avatar" style="background:#3B82F6">GR</div></div></div>'
    '<div class="kanban-card" style="opacity:0.7"><div class="kanban-card-title">Sess&atilde;o 1 gravada</div>'
    '<div class="kanban-card-meta"><span class="kanban-card-tag" style="background:#DCFCE7;color:#166534">Fase 1</span>'
    '<div class="kanban-card-avatar" style="background:#3B82F6">GR</div></div></div>'
    '</div>'
    '</div>'
)

# --- AGENDA (CALENDAR) ---
agenda_html = (
    '<div class="portal-greeting">Agenda do Programa</div>'
    '<div class="portal-box" style="margin-bottom:clamp(0.3rem,0.5vh,0.4rem);padding:clamp(0.4rem,0.7vh,0.6rem)">'
    '<div class="cal-header"><span style="font-weight:600">Mar&ccedil;o 2026</span>'
    '<div class="cal-header-nav"><button class="cal-header-btn">&lsaquo;</button><button class="cal-header-btn">&rsaquo;</button></div></div>'
    '<div class="cal-grid">'
    '<div class="cal-day-label">Seg</div><div class="cal-day-label">Ter</div><div class="cal-day-label">Qua</div>'
    '<div class="cal-day-label">Qui</div><div class="cal-day-label">Sex</div><div class="cal-day-label">S&aacute;b</div><div class="cal-day-label">Dom</div>'
    # Week 1 (March starts on Sunday)
    '<div class="cal-day other-month">23</div><div class="cal-day other-month">24</div><div class="cal-day other-month">25</div>'
    '<div class="cal-day other-month">26</div><div class="cal-day other-month">27</div><div class="cal-day other-month">28</div><div class="cal-day">1</div>'
    # Week 2
    '<div class="cal-day today">2</div><div class="cal-day">3</div><div class="cal-day">4</div>'
    '<div class="cal-day">5</div><div class="cal-day">6</div><div class="cal-day">7</div><div class="cal-day">8</div>'
    # Week 3
    '<div class="cal-day">9</div><div class="cal-day">10</div><div class="cal-day">11</div>'
    '<div class="cal-day">12</div><div class="cal-day">13</div><div class="cal-day">14</div><div class="cal-day">15</div>'
    # Week 4
    '<div class="cal-day">16</div><div class="cal-day">17</div><div class="cal-day has-event">18</div>'
    '<div class="cal-day">19</div><div class="cal-day">20</div><div class="cal-day">21</div><div class="cal-day">22</div>'
    # Week 5
    '<div class="cal-day">23</div><div class="cal-day">24</div><div class="cal-day">25</div>'
    '<div class="cal-day">26</div><div class="cal-day">27</div><div class="cal-day">28</div><div class="cal-day">29</div>'
    # Week 6
    '<div class="cal-day">30</div><div class="cal-day">31</div><div class="cal-day has-event" style="background:#FEF3C7;color:#92400E;font-weight:600">1</div>'
    '<div class="cal-day other-month">2</div><div class="cal-day other-month">3</div><div class="cal-day other-month">4</div><div class="cal-day other-month">5</div>'
    '</div></div>'
    # Upcoming events
    '<div class="portal-box-title" style="margin-bottom:clamp(0.15rem,0.3vh,0.2rem)">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg>'
    'Pr&oacute;ximos Encontros</div>'
    '<div class="cal-events">'
    '<div class="cal-event"><div class="cal-event-dot" style="background:#472D07"></div>'
    '<div class="cal-event-date">18/03</div><div><div class="cal-event-title">Panorama IA + Demos</div>'
    '<div class="cal-event-time">14h&ndash;18h &middot; Online</div></div></div>'
    '<div class="cal-event"><div class="cal-event-dot" style="background:#3B82F6"></div>'
    '<div class="cal-event-date">01/04</div><div><div class="cal-event-title">Mapeamento de Oportunidades</div>'
    '<div class="cal-event-time">14h&ndash;18h &middot; Presencial</div></div></div>'
    '<div class="cal-event"><div class="cal-event-dot" style="background:#22C55E"></div>'
    '<div class="cal-event-date">15/04</div><div><div class="cal-event-title">Workshop Champions</div>'
    '<div class="cal-event-time">14h&ndash;18h &middot; Online</div></div></div>'
    '</div>'
)

# --- PROJETOS (modernized) ---
projetos_html = (
    '<div class="portal-greeting">Projetos Ativos</div>'
    '<div class="portal-cards">'
    '<div class="portal-stat-card"><div style="display:flex;align-items:center;justify-content:space-between">'
    '<div><div class="stat-label">Em Andamento</div><div class="stat-value" style="color:#3B82F6">5</div></div>'
    '<div style="width:clamp(28px,3.5vw,38px);height:clamp(28px,3.5vw,38px);border-radius:50%;background:linear-gradient(135deg,#EFF6FF,#DBEAFE);display:flex;align-items:center;justify-content:center">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#3B82F6" stroke-width="2"><path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/></svg></div></div></div>'
    '<div class="portal-stat-card"><div style="display:flex;align-items:center;justify-content:space-between">'
    '<div><div class="stat-label">Conclu&iacute;dos</div><div class="stat-value" style="color:#22C55E">3</div></div>'
    '<div style="width:clamp(28px,3.5vw,38px);height:clamp(28px,3.5vw,38px);border-radius:50%;background:linear-gradient(135deg,#F0FDF4,#DCFCE7);display:flex;align-items:center;justify-content:center">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#22C55E" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div></div></div>'
    '<div class="portal-stat-card"><div style="display:flex;align-items:center;justify-content:space-between">'
    '<div><div class="stat-label">Empresas</div><div class="stat-value">4</div></div>'
    '<div style="width:clamp(28px,3.5vw,38px);height:clamp(28px,3.5vw,38px);border-radius:50%;background:linear-gradient(135deg,#F0EDE8,#E8E2D6);display:flex;align-items:center;justify-content:center">'
    '<svg width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="#472D07" stroke-width="2"><path d="M3 21h18"/><path d="M9 8h1"/><path d="M9 12h1"/><path d="M9 16h1"/><path d="M14 8h1"/><path d="M14 12h1"/><path d="M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16"/></svg></div></div></div>'
    '</div>'
    # Project list
    '<div style="display:flex;flex-direction:column;gap:clamp(0.2rem,0.4vh,0.3rem)">'
    '<div class="portal-box" style="padding:clamp(0.35rem,0.6vh,0.5rem) clamp(0.4rem,0.7vw,0.6rem)">'
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px">'
    '<span style="font-size:clamp(0.5rem,0.65vw,0.62rem);font-weight:600;color:#1a1a1a">Agente de Estoque &mdash; Tecnotri</span>'
    '<span class="kanban-card-tag" style="background:#DBEAFE;color:#1E40AF">Em andamento</span></div>'
    '<div class="portal-proj-bar"><div class="portal-proj-fill" style="width:65%;background:#3B82F6"></div></div>'
    '<div class="portal-proj-meta">Rafaela Lopes &middot; 65% &middot; Previs&atilde;o: Abril</div></div>'
    '<div class="portal-box" style="padding:clamp(0.35rem,0.6vh,0.5rem) clamp(0.4rem,0.7vw,0.6rem)">'
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px">'
    '<span style="font-size:clamp(0.5rem,0.65vw,0.62rem);font-weight:600;color:#1a1a1a">Automa&ccedil;&atilde;o NF &mdash; Robustec</span>'
    '<span class="kanban-card-tag" style="background:#FEF3C7;color:#92400E">Planejamento</span></div>'
    '<div class="portal-proj-bar"><div class="portal-proj-fill" style="width:20%;background:#EAB308"></div></div>'
    '<div class="portal-proj-meta">Marcos Caldeira &middot; 20% &middot; Previs&atilde;o: Maio</div></div>'
    '<div class="portal-box" style="padding:clamp(0.35rem,0.6vh,0.5rem) clamp(0.4rem,0.7vw,0.6rem)">'
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:3px">'
    '<span style="font-size:clamp(0.5rem,0.65vw,0.62rem);font-weight:600;color:#1a1a1a">Dashboard BI &mdash; Gallus</span>'
    '<span class="kanban-card-tag" style="background:#DBEAFE;color:#1E40AF">Em andamento</span></div>'
    '<div class="portal-proj-bar"><div class="portal-proj-fill" style="width:45%;background:#3B82F6"></div></div>'
    '<div class="portal-proj-meta">Jo&atilde;o P. &middot; 45% &middot; Previs&atilde;o: Abril</div></div>'
    '</div>'
)

# Apply all view replacements
html = replace_view(html, 'view-dashboard', dashboard_html)
html = replace_view(html, 'view-biblioteca', trilhas_html)
html = replace_view(html, 'view-champions', comunidade_html)
html = replace_view(html, 'view-projetos', projetos_html)
html = replace_view(html, 'view-tarefas', tarefas_html)
html = replace_view(html, 'view-agenda', agenda_html)

# Update view IDs to match new data-view attributes
html = html.replace('id="view-biblioteca"', 'id="view-trilhas"')
html = html.replace('id="view-champions"', 'id="view-comunidade"')

# ============================================================
# 4. FIX JS — update view IDs referenced in JavaScript
# ============================================================
# The initPortal JS references 'view-' + dataView, so if sidebar has
# data-view="trilhas", the JS will look for id="view-trilhas" (which we renamed above)
# This should work automatically since the JS uses:
# document.getElementById('view-' + dataView)

# Also update the count-up animation which references #view-dashboard
# This should still work since we kept id="view-dashboard"

with open('proposta-colloni-slides.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone! File size: {len(html)} bytes')
