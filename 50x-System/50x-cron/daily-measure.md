Generate today's 50x dashboard.

## Step 1: Run the measure script
```bash
~/.hermes/bin/50x-measure.sh today > /tmp/today-50x.txt
```

## Step 2: Parse the output
Read /tmp/today-50x.txt. Extract:
- Total applications today
- Top 3 patterns
- Any new dead patterns
- Productivity delta estimate

## Step 3: Append to the dashboard
Append a section to ~/.hermes/50x-dashboard.md:
```
## YYYY-MM-DD

- **Applications today:** N
- **Top helper:** P## (X helped)
- **Top harm:** P## (Y harmful)
- **Delta vs yesterday:** ↑/↓ Z×

<3-bullet summary>
```

## Step 4: Post to Telegram
3 bullets only:
- 📊 Today: N applications
- 🏆 Top helper: P## <name> (X helped)
- 📈 Delta: Z× (vs Y× yesterday)

If delta is up > 20%, add: "🔥 Best day this week."
If delta is down > 20%, add: "⚠️ Investigate — what's blocking?"

## Skills used
- file, terminal

## Deliver
- telegram (the 3 bullets)
- local (the full dashboard append)
