# Keep native AFM timing, choice stops and text display; no synthetic dismiss timer.
# In this custom UI, 8.5.3's compatibility init at 1100 clears the enable toggle.
# Restore its explicit mode before SDK defaults apply at 1500, without changing
# the other script compatibility behaviors or a saved reader interval.
init 1200 python:
    config.default_afm_enable = False

init -5 python:
    class StoryAutoToggle(Action):
        def __call__(self):
            # Zero disables native AFM. Repair it only on an explicit enabling click.
            # Existing positive reader intervals remain untouched.
            if not _preferences.afm_enable and not _preferences.afm_time:
                Preference('auto-forward time', 15)()
            Preference('auto-forward', 'toggle')()

        def get_selected(self):
            return bool(_preferences.afm_enable)
