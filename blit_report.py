import pygame
from display_vars import screen, screen_w, screen_h
from buttons import NextButton
from fonts import head_font, reg_font

report_x = screen_w/5
report_w = screen_w - (screen_w/5)*2
report_y = 100
report_h = screen_h - 100*2
report_rect = pygame.Rect(report_x, report_y, report_w, report_h)
next_btn = NextButton(report_x + report_w/2.6, report_y + report_h - 140, 300, 100, (0, 255, 0), "Next")

def blit_report(colony, week, season, report_type):
    if week in [5, 9, 13]:
        show_week = 1
    elif week in [4, 8, 12, 16]:
        show_week = 4
    else:
        show_week = week % 4
    show_report = True
    season_display = head_font.render(season, True, (0, 0, 0))
    if report_type == "weekly":
        title = "Weekly Report"
        report = colony.weekly_report
    elif report_type == "seasonal":
        title = "Seasonal Report"
        report = colony.seasonal_report
    elif report_type == "annual":
        title = "Annual Report"
        report = colony.annual_report
    title_display = head_font.render(title, True, (0, 0, 0))
    week_display = head_font.render("Week: " + str(show_week), True, (0, 0, 0))
    name_display = head_font.render(colony.name, True, (0, 0, 0))

    while show_report:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            show_report = next_btn.handle_event(event)
        screen.fill((98, 130, 122))
        pygame.draw.rect(screen, (255, 255, 255), report_rect)
        screen.blit(name_display, (report_x + 40 + report_w/5.6, report_y + 40))
        screen.blit(title_display, (report_x + 40 + report_w/3.5, report_y + 130))
        screen.blit(season_display, (report_x + 365, report_y + 220))
        screen.blit(week_display, (report_x + 615, report_y + 220))
        key_x = report_x + 80
        y = report_y + 330
        value_x = report_x + report_w - 100
        for key, value in report.items():
            value_x = report_x + report_w - 100
            key_display = reg_font.render(f"{key}: ", True, (0, 0, 0))
            if value > 0:
                value_display = reg_font.render("+" + str(value), True, (0, 0, 0))
            else:
                value_display = reg_font.render(str(value), True, (0, 0, 0))
            screen.blit(key_display, (key_x, y))
            screen.blit(value_display, (value_x, y))
            y += 40
        next_btn.draw(80)
        pygame.display.update()

