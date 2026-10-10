# 仅显示名字；剧情原文、角色ID、模型ID、存档键与API参数保持原值。
init 950 python:
    _v17_previous_replace_text = config.replace_text

    def v17_display_text(text):
        if _v17_previous_replace_text is not None:
            text = _v17_previous_replace_text(text)
        if not isinstance(text, str):
            return text
        return text.replace('DeepSeek', '鲸鱼娘').replace('Qwen', '千问大小姐')

    config.replace_text = v17_display_text
