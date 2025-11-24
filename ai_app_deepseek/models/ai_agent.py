# -*- coding: utf-8 -*-
from odoo import _, api, Command, fields, models


class AIAgent(models.Model):
    _inherit = 'ai.agent'

    def _build_extra_system_context(self, discuss_channel):
        """
            The original method <_build_extra_system_context> fixed this value <ai.ai_agent_natural_language_search> directly,
             which makes it difficult to extend.
        """
        self.ensure_one()
        if self.llm_model in ['deepseek-chat', 'deepseek-reasoner']:
            extra_context = []
            topic_xml_ids = self.topic_ids.get_external_id().values()
            if any(topic in ["ai.ai_topic_natural_language_query", "ai.ai_topic_information_retrieval_query"] for topic in topic_xml_ids):
                extra_context.append(self._get_available_models())
            if self.get_external_id()[self.id] == "ai_ask_deepseek.ai_agent_natural_language_search":
                extra_context.append(self._get_available_menus())
                extra_context.append(self._get_date_calculation_reference())
            elif env_context := discuss_channel.ai_env_context:
                extra_context += env_context
            return "\n".join(extra_context) if extra_context else ""
        else:
            return super()._build_extra_system_context(discuss_channel)

