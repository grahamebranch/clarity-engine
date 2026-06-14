from rameon_core.engine.simple_engine import SimpleEngine

engine = SimpleEngine()

text = (
    "so basically I was thinking that maybe the project could sort of be restarted "
    "but not fully restarted because some parts are fine but also not really fine "
    "because people didn’t follow the guidelines and then we had that meeting which "
    "honestly didn’t help because everyone was talking over each other and nobody "
    "wrote anything down so now we’re kind of in this weird place where we need to "
    "decide what to do but nobody wants to decide because they’re worried about "
    "making the wrong decision and also the timeline is kind of a mess and I think "
    "we should maybe pause but not really pause just slow down but also speed up in "
    "some areas because otherwise we’ll fall behind but also maybe we’re already "
    "behind I don’t know it’s all a bit confusing and I think someone needs to take "
    "charge but I don’t want to be the one to say that because it might sound rude."
)

result = engine.run_composite_test(text)

print(result["final_text"])
