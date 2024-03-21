PennController.ResetPrefix(null);

Sequence("instructions", "practice", "testComplete", randomize("trial"), SendResults(), "final");

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

// Practice trials
Template("practice_list.csv", row => 
    newTrial("practice",
        newText("forwardMask", "######")
            .print()
            .settings.css("font-size", "2em"),
        newTimer("forwardMaskTimer", 500)
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
    .log("group", row.itemGroup)
    .log("condition", row.condition)
    .log("prime", row.prime)
    .log("target", row.target)
    .log("primetype", row.primetype)
);

// Intermediate screen after completing practice trials
newTrial("testComplete",
    newText("testCompleteText", "You have completed the practice trials. Now you will begin the actual test cases.")
        .print()
        .center()
        .css("font-size", "1em"),
    newText("testCompleInstruction", "Press the space bar to begin a practice session."),
    newKey("start", " ")
        .wait()
);

// Function to select a list based on a random assignment
const selectList = () => {
    const listNumber = Math.ceil(Math.random() * 4); // Randomly select a number between 1 and 4
    return 'newlist' + listNumber + '.csv'; // Return the filename of the list
};

// Load the randomly selected list for this participant
Template(selectList(), row => 
    newTrial("trial",
        newText("forwardMask", "######")
            .print()
            .settings.css("font-size", "2em"),
        newTimer("forwardMaskTimer", 500)
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
    .log('group', row.itemGroup)
    .log("condition", row.condition)
    .log("prime", row.prime)
    .log("target", row.target)
    .log("primetype", row.primetype)
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
