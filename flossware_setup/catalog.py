"""Static, provider-neutral setup catalogs.

Domain data only: agent adapters, capabilities, budget policies, and providers.
No I/O, no credentials, no UI.
"""

from __future__ import annotations

from dataclasses import dataclass

FLOSSWARE_BASE = "https://github.com/FlossWare"


@dataclass(frozen=True)
class AgentAdapter:
    """Metadata and project instruction targets for a coding agent."""

    id: str
    name: str
    description: str
    files: tuple[str, ...]


AGENTS: tuple[AgentAdapter, ...] = (
    AgentAdapter("claude-code", "Claude Code", "Anthropic project instructions", ("CLAUDE.md",)),
    AgentAdapter("cursor", "Cursor", "Cursor project rules", (".cursorrules",)),
    AgentAdapter("opencode", "OpenCode", "Shared agent instructions", ("AGENTS.md",)),
    AgentAdapter("crush", "Crush", "Shared project context", ("AGENTS.md",)),
    AgentAdapter("codex", "Codex", "OpenAI project instructions", ("AGENTS.md",)),
    AgentAdapter("aider", "Aider", "Aider conventions", ("CONVENTIONS.md",)),
    AgentAdapter("cline", "Cline", "Cline project rules", (".clinerules/FlossWare.md",)),
    AgentAdapter("roo-code", "Roo Code", "Roo Code project rules", (".roo/rules/FlossWare.md",)),
    AgentAdapter("gemini-cli", "Gemini CLI", "Gemini project instructions", ("GEMINI.md",)),
    AgentAdapter("github-copilot", "GitHub Copilot", "GitHub repository instructions", (".github/copilot-instructions.md",)),
    AgentAdapter("windsurf", "Devin Desktop", "Devin Desktop rules under .devin/rules/", (".devin/rules/FlossWare.md",)),
    AgentAdapter("amazon-q", "Amazon Q Developer", "Amazon Q project rules", (".amazonq/rules/FlossWare.md",)),
    AgentAdapter("kiro", "Kiro", "Kiro workspace steering", (".kiro/steering/FlossWare.md",)),
)

AGENT_BY_ID: dict[str, AgentAdapter] = {a.id: a for a in AGENTS}

CAPABILITIES: tuple[tuple[str, str, bool], ...] = (
    ("model-gateway", "LLM routing, provider failover, capability and cost awareness", True),
    ("resilience", "Retry, circuit breakers, timeouts", True),
    ("output-validation", "Schema-validated model output", True),
    ("consensus", "Multi-model voting", False),
    ("evaluation", "Quality scoring and adversarial verification", False),
    ("observability", "Structured logging, metrics, cost tracking", False),
    ("security", "Validation, secret masking, audit logging", False),
    ("rag", "Document retrieval and hybrid search", False),
    ("optimization", "Genetic optimization", False),
)

CAPABILITY_BY_ID: dict[str, tuple[str, str, bool]] = {c[0]: c for c in CAPABILITIES}

CAPABILITY_REFS: dict[str, str] = {
    "model-gateway": "98ea2b3d27c483b7d77ad5770d097a79872c3785",
    "resilience": "d6253a6bc80941a02015c94c63c70c32d7cc0549",
    "output-validation": "0b5e21dd9c94eb41a49eede6ba6d865a261707d2",
    "consensus": "4570e0429c4abee5a6b68d964786cb90e07282d8",
    "evaluation": "368c222f60a491e5022f8472d954c947bd47a9bf",
    "observability": "c4c563da098aa75d4789069fe523403fdd8bd9be",
    "security": "79c11558f39e966f15d0c50a955acded2e252f32",
    "rag": "8bc0f6ae899b39ae6708c7b158d82529adbc2209",
    "optimization": "3044c7cdb88a2aa4b6278b35ec92d8a61b79d5f3",
}

BUDGET_POLICIES: tuple[tuple[str, str, float, str], ...] = (
    ("strict", "Strict budget", 0.0, "Only providers/models permitted by a zero-cost policy"),
    ("light", "Light", 10.0, "Up to $10/month"),
    ("medium", "Medium", 50.0, "Up to $50/month"),
    ("custom", "Custom", -1.0, "Set an explicit monthly ceiling"),
)

BUDGET_BY_ID: dict[str, tuple[str, str, float, str]] = {b[0]: b for b in BUDGET_POLICIES}

# Keep this catalog synchronized with model-gateway's provider definitions.
# This metadata catalog must include Anthropic so ANTHROPIC_API_KEY and Claude
# models are visible to the setup UI. It never reads or stores secret values.
PROVIDERS: tuple[tuple[str, str, str], ...] = (
    ("Anthropic", "ANTHROPIC_API_KEY", "https://console.anthropic.com/settings/keys"),
    ("OpenAI", "OPENAI_API_KEY", "https://platform.openai.com/api-keys"),
    ("OpenRouter", "OPENROUTER_API_KEY", "https://openrouter.ai/keys"),
    ("Groq", "GROQ_API_KEY", "https://console.groq.com/keys"),
    ("Cerebras", "CEREBRAS_API_KEY", "https://cloud.cerebras.ai/"),
    ("DeepInfra", "DEEPINFRA_API_TOKEN", "https://deepinfra.com/dash/api_keys"),
    ("NVIDIA", "NVIDIA_API_KEY", "https://build.nvidia.com/settings/api-keys"),
    ("Gemini", "GEMINI_API_KEY", "https://aistudio.google.com/apikey"),
    ("Cohere", "COHERE_API_KEY", "https://dashboard.cohere.com/api-keys"),
    ("HuggingFace", "HUGGINGFACE_API_KEY", "https://huggingface.co/settings/tokens"),
)
