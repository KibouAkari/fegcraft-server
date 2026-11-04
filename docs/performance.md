# Performance

The production stack already included Lithium, C2ME, FerriteCore, ModernFix, Noisium, ServerCore, Chunky and spark. Do not add duplicate optimization mods blindly.

Measure MSPT/TPS and spark profiles **under real player load** before interpreting bottlenecks. The CPU is an older 4-core i7 and the host uses rotational disks shared with other services. Fast exploration in several dimensions may be constrained by CPU main-thread work, world generation and disk I/O.

A 2.4 logical-CPU cap was applied live with `docker update --cpus 2.4`. That alone does not guarantee persistence if Compose recreates the container; document the validated production resource definition before copying the setting. The live JVM had 6 GiB initial / 24 GiB maximum heap, so adding a lower hard memory cap without modifying the JVM can cause OOM termination.

For the staged view/simulation distances see [runtime snapshot](runtime.md). Some changes take effect only on the next Minecraft start and may affect farms and gameplay.
