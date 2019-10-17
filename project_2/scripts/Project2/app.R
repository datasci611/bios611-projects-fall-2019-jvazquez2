library(shiny)

# Loading helper functions
source("F:\\UNC\\FALL 2019\\BIOS 611\\bios611-homework-fall-2019-jvazquez2\\homework\\HW4_helper.R")
mydata = loaddata()

# Define UI for app that draws a histogram and a data table----
ui <- fluidPage(
    
    # App title ----
    titlePanel("Chapel Hill: Police"),
    
    # Sidebar layout with input and output definitions ----
    sidebarLayout(
        
        # Sidebar panel for inputs ----
        sidebarPanel(
            
            # Input: Integer for the number of bins ----
            radioButtons("CheckGroup", 
                         h3("Checkbox group"),
                         choices = list("City" = "City",
                                        "Victim Gender" = "VictimGender",
                                        "Victim Race" = "VictimRace"),
                         selected = "City"), textOutput("uniquevalues")
        ),
        
        # Main panel for displaying outputs ----
        mainPanel(
            # Output: Histogram and table----
            plotOutput(outputId = "popPlot")
        )
    )
)

# Define server logic required to draw a histogram ----
server <- function(input, output) {
    # renderPlot creates histogram and links to ui
    output$popPlot <- renderPlot({
        f(input$CheckGroup)
    })
    output$uniquevalues <- renderText({
        myvariable <- length(unique(mydata[[input$CheckGroup]]))
        paste("The number of values from this variable is", myvariable)
    })
}

shinyApp(ui = ui, server = server)
