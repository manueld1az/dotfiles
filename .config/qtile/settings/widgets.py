from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(fg='focus'), linewidth=3, padding=5)

def separatorInvisible():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=15, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=1
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=50,
        padding=-8
    )


def workspaces(): 
    return [
        widget.GroupBox(
            **base(fg='light'),
            font='JetBrainsMono Nerd Font',
            fontsize=15,
            margin_y=3,
            margin_x=0,
            padding_y=3,
            padding_x=3,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='line',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['color5'],
            this_screen_border=colors['focus'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        separatorInvisible(),
        widget.Prompt(),
        widget.WindowName(**base(fg='text'), fontsize=15, padding=5),
        separatorInvisible(),
    ]


primary_widgets = [
    *workspaces(),

    powerline('color5', 'dark'),

    icon(bg="color5", text=' '),
    
    widget.CheckUpdates(
        background=colors['color5'],
        colour_have_updates=colors['dark'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color4', 'color5'),

    icon(bg="color4", text='龍 '),
    
    widget.Net(**base(bg='color4'),width=170, format='{down:6.2f}kb{up:6.2f}kb', interface='enp4s0', prefix='k'),

    powerline('color3', 'color4'),

    icon(bg="color3", text=''),

    widget.ThermalSensor(
            background=colors['color3'],
            threshold=50,
            tag_sensor="gigabyte_wmi-2",
            fmt='{}',
        ),

    icon(bg="color3", text=''),

    widget.ThermalSensor(
            background=colors['color3'],
            threshold=50,
            #Sensor del CPU
            #tag_sensor="Tctl",
            tag_sensor="gigabyte_wmi-5",
            fmt='{}',
        ),

    widget.ThermalSensor(
            background=colors['color3'],
            threshold=50,
            tag_sensor="edge",
            fmt=' {}',
        ),

    #powerline('color3', 'color4'),

    #icon(bg="color3", text=' '),

    #widget.Memory(background=colors['color4']),

    powerline('color2', 'color3'),

    icon(bg="color2", fontsize=15, text=' '),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('color1', 'color2'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=1),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=1),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'JetBrainsMono Nerd Font',
    'fontsize': 15,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
