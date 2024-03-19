PennController.ResetPrefix(null);

Sequence("instructions", "practice", randomize("trial"), SendResults(), "final");

// Instructions trial
newTrial("instructions",
    defaultText
        .print()
        .center()
        .css("font-size", "1em"),
    newText("instruction1", "Welcome to the experiment. In this task, you will be asked to decide whether a sequence of letters forms a real English word."),
    newText("instruction2", "Press 'F' if you think the sequence is a word, and 'J' if you think it is not a word."),
    newText("instruction3", "Press the space bar to begin a practice session."),
    newKey("start", " ")
        .wait()
);

Template("practice_list.csv", row => 
    newTrial("practice",
        newText("forwardMask", "######")
            .print()
            .settings.css("font-size", "2em"),
        newTimer("forwardMaskTimer", 5000)
            .start()
            .wait(),
        getText("forwardMask").remove(),

        newText("prime", row.prime.toLowerCase())
            .print()
            .settings.css("font-size", "2em"),
        newTimer("primeTimer", 400)
            .start()
            .wait(),
        getText("prime").remove(),

        newText("backwardMask", "######")
            .print()
            .settings.css("font-size", "2em"),
        newTimer("backwardMaskTimer", 400)
            .start()
            .wait(),
        getText("backwardMask").remove(),

        newText("target", row.target.toUpperCase())
            .print()
            .settings.css("font-size", "2em"),
        
        newKey("response", "FJ")
            .log("all")
            .wait(),

        getText("target").remove()
    )
    .log("group", row.group)
    .log("condition", row.condition)
    .log("prime", row.prime)
    .log("target", row.target)
    .log("primetype", row.primetype)
);


// Experimental trials
Template("list.csv", row => 
    newTrial("trial",
        newText("forwardMask", "######")
            .print()
            .settings.css("font-size", "2em"),
        newTimer("forwardMaskTimer", 5000)
            .start()
            .wait(),
        getText("forwardMask").remove(),

        newText("prime", row.prime.toLowerCase())
            .print()
            .settings.css("font-size", "2em"),
        newTimer("primeTimer", 400)
            .start()
            .wait(),
        getText("prime").remove(),

        newText("backwardMask", "######")
            .print()
            .settings.css("font-size", "2em"),
        newTimer("backwardMaskTimer", 400)
            .start()
            .wait(),
        getText("backwardMask").remove(),

        newText("target", row.target.toUpperCase())
            .print()
            .settings.css("font-size", "2em"),
        
        newKey("response", "FJ")
            .log("all") // Log all properties, including the pressed key and response time
            .wait(),

        getText("target").remove()
    )
    .log("Group", row.group)
    .log("Condition", row.condition)
    .log("Prime", row.prime)
    .log("Target", row.target)
    // The 'Response' and 'RT' are logged as part of the newKey command
);

// Send results
SendResults("send");

// Final screen
newTrial("final",
    newText("Thank you for participating in the experiment. You can now close this window.")
        .print()
        .center(),
    newButton("end", "Close")
        .print()
        .wait()
);