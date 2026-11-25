# Marketing Agent Skills

**Practical, read-only AI assistant skills for growth marketing, paid media, SEO, CRO and reporting.**

An independent, open-format collection by Adam Amrullah, a growth marketer and AI-assisted product builder. The goal is repeatable, evidence-based marketing workflows with clear human approval boundaries.

## Skill library

| Skill | Purpose | Example |
| --- | --- | --- |
| [google-ads-audit](skills/google-ads-audit/SKILL.md) | Audit Google Ads account performance and search terms, flag tracking issues, and produce a prioritized read-only optimization plan | [Fixture](skills/google-ads-audit/examples/example.md) |
| [meta-ads-audit](skills/meta-ads-audit/SKILL.md) | Audit Meta Ads campaigns, creative performance and funnel signals, with a read-only optimization plan | [Fixture](skills/meta-ads-audit/examples/example.md) |
| [seo-content-audit](skills/seo-content-audit/SKILL.md) | Review Google Search Console and site content for actionable SEO opportunities, content decay, and possible keyword cannibalization | [Fixture](skills/seo-content-audit/examples/example.md) |
| [paid-media-budget-allocation](skills/paid-media-budget-allocation/SKILL.md) | Propose scenario-based paid media budget allocation across campaigns or channels with explicit uncertainty, constraints and approval gates | [Fixture](skills/paid-media-budget-allocation/examples/example.md) |
| [competitor-analysis](skills/competitor-analysis/SKILL.md) | Create evidence-based competitive positioning and messaging analysis from supplied or authorized public sources | [Fixture](skills/competitor-analysis/examples/example.md) |
| [landing-page-audit](skills/landing-page-audit/SKILL.md) | Audit landing page clarity, conversion UX, message match and measurement; produce a prioritized CRO plan | [Fixture](skills/landing-page-audit/examples/example.md) |
| [marketing-experiment-planner](skills/marketing-experiment-planner/SKILL.md) | Design measurable marketing experiments with hypotheses, success metrics, guardrails and decision rules | [Fixture](skills/marketing-experiment-planner/examples/example.md) |
| [campaign-performance-report](skills/campaign-performance-report/SKILL.md) | Turn comparable marketing performance exports into an executive report with transparent calculations, insights and next actions | [Fixture](skills/campaign-performance-report/examples/example.md) |

## Quick start

### Any assistant supporting file uploads

1. Open the relevant skill folder and attach its `SKILL.md` to an AI chat (and the example if testing).
2. Supply a sanitized export or brief. Do not include API keys or identifiable customer records.
3. Prompt: `Use the attached skill as guidance. Analyze the supplied data, label assumptions, and return the specified deliverable. Do not modify accounts.`
4. Review calculations, sources and recommendations before taking action.

### Native Agent Skills hosts

Each folder includes a `SKILL.md` with `name` and `description` front matter. Copy the entire chosen skill folder into your host's documented skills location (for example, a Claude Code project's `.claude/skills/` directory). Exact discovery, permissions and execution vary by host. This repository has not been integration-tested with any particular host. File attachment alone is not permanent installation.

## Scope and limitations

- These are instruction-based skills, not API connectors, autonomous agents, or live advertising integrations.
- All examples are synthetic; acceptance criteria are expected behavior, not model execution results.
- Use read-only exports or authorized read-only integrations. No budget edits, negative keywords, publishing or account mutations without separate approval.
- Platform data is attribution-dependent; reports should distinguish attributed outcomes from incremental impact.
- No guaranteed marketing lift, ranking, or financial outcomes.

## Validation

Run `python -m unittest discover -s tests -v` from the repository root (Python 3.10+, no dependencies). This verifies package structure, front matter, required sections and fixture links. It does not validate LLM output quality or platform compatibility. To evaluate a skill, run its example with your target assistant and manually check the acceptance criteria.

## Contributing

Propose improvements using synthetic or appropriately anonymized data. Include a fixture, clear expected behavior, and explicit approval boundaries. Do not commit secrets, production exports or copyrighted client material.

## License

MIT — see [LICENSE](LICENSE). Independent project; not affiliated with Google, Meta, or any assistant provider.

Related: [Lovable PRD Generator](https://github.com/adamamrullah/lovable-prd-generator) · [GSC Opportunity Analyzer](https://github.com/adamamrullah/gsc-opportunity-analyzer) · [Boost With AI](https://boostwithai.se/)
