"""
Item data for display cards, organized by category
"""

# Complete list of items with their categories and fun facts
ITEMS = [
    # Minerals & Fossils
    ("Minerals & Fossils", "Dinosaur fossil", "Some fossils are over 230 million years old, formed when minerals replace organic material."),
    ("Minerals & Fossils", "Blue calcite", "Gets its color from copper and can glow under ultraviolet light."),
    ("Minerals & Fossils", "Honey calcite", "Creates a double-refraction effect that makes images appear twice."),
    ("Minerals & Fossils", "Labradorite", "Shimmering colors come from light scattering within layered crystal structure."),
    ("Minerals & Fossils", "Spectralite", "A rare Finnish labradorite with the most colorful iridescence of any feldspar."),
    ("Minerals & Fossils", "Red ammonite", "Marine predators that survived for over 300 million years before extinction."),
    ("Minerals & Fossils", "Purple agate", "Forms inside volcanic rock cavities when silica-rich water deposits layers over millennia."),
    ("Minerals & Fossils", "Hourglass selenite", "So soft you can scratch it with a fingernail; named after the Greek moon goddess."),
    ("Minerals & Fossils", "Desert Rose Crystal", "Forms in arid conditions as evaporating water leaves behind gypsum crystals."),
    ("Minerals & Fossils", "Wulfenite crystal", "Vibrant orange-red color comes from traces of molybdenum."),
    
    # Shells & Marine
    ("Shells & Marine", "Yellow dog conch shell", "Named for tooth-like projections around its opening."),
    ("Shells & Marine", "Butter clam shell", "Can live up to 20 years and dig several inches into seafloors with their 'foot'."),
    ("Shells & Marine", "Brooch clamshell", "Growth rings similar to tree rings reveal age and historical climate patterns."),
    ("Shells & Marine", "Conch shell eggs", "Called 'mermaid's necklaces,' containing hundreds of eggs in a protective string."),
    ("Shells & Marine", "Horseshoe crab", "Living fossils unchanged for 450 million years, predating dinosaurs."),
    ("Shells & Marine", "Shark jaw", "Sharks can go through up to 30,000 teeth in a lifetime."),
    
    # Plant Materials
    ("Plant Materials", "Sugar pinecones", "Produce the longest cones of any conifer, sometimes exceeding 2 feet."),
    ("Plant Materials", "Pine cones", "Actually the tree's reproductive organs, with male and female versions."),
    ("Plant Materials", "Bottle tree seed pods", "From trees with swollen trunks that store water for survival in arid regions."),
    ("Plant Materials", "Moss", "Can absorb up to 20 times its weight in water despite having no roots."),
    ("Plant Materials", "Okra seed pods", "Produce a natural mucilage once used in emergency blood transfusions during WWII."),
    ("Plant Materials", "Driftwood", "Can float in oceans for years, traveling thousands of miles before washing ashore."),
    ("Plant Materials", "Foxtails", "Have barbed seeds that can only move forward, frequently becoming embedded in animal fur."),
    
    # Preserved Specimens
    ("Preserved Specimens", "Duckling", "Preserved in liquids like formaldehyde, a technique dating back to the 17th century."),
    ("Preserved Specimens", "Mummified Duckling", "Natural mummification occurs when bodies dry quickly in arid conditions."),
    ("Preserved Specimens", "Chipmunk", "Can gather up to 165 acorns daily, storing thousands in underground chambers."),
    ("Preserved Specimens", "Opossum", "Naturally immune to rabies and can eat up to 5,000 ticks yearly."),
    ("Preserved Specimens", "Chameleon", "Tongue accelerates faster than a space shuttle, reaching prey in under 0.07 seconds."),
    ("Preserved Specimens", "Snakeskin", "Snakes shed their entire skin in one piece, including eye scales."),
    ("Preserved Specimens", "Chick", "Modern methods use specialized foam forms rather than traditional wood wool."),
    ("Preserved Specimens", "Weasel", "Must eat about 40% of their body weight daily due to fast metabolism."),
    ("Preserved Specimens", "Fox head", "Foxes have whiskers on their legs as well as faces for navigating in darkness."),
    ("Preserved Specimens", "Chinese water dragon", "Can stay underwater for up to 25 minutes using tails as rudders."),
    
    # Animal Parts
    ("Animal Parts", "Macaw feathers", "Colors come from microscopic structures reflecting specific light wavelengths."),
    ("Animal Parts", "Goose feathers", "Once valuable writing tools used for quill pens from the 6th to 19th century."),
    ("Animal Parts", "Turtle shell", "Actually part of the skeleton, fused with ribs, vertebrae, and collarbone."),
    ("Animal Parts", "Bird's nest", "Some birds incorporate medicinal plants that repel parasites to protect their young."),
    ("Animal Parts", "Wasp nest", "Built by chewing wood fibers mixed with saliva, essentially creating paper maché."),
    ("Animal Parts", "Cobra skin", "Distinctive hood formed by elongated ribs that extend when threatened."),
    ("Animal Parts", "Butterfly and moth wings laminated", "A single wing can contain more than 100,000 tiny scales."),
    ("Animal Parts", "Snake shed", "Snakes typically shed 4-12 times yearly, with younger snakes shedding more frequently."),
    ("Animal Parts", "Beaver paw", "Front paws are remarkably dexterous, able to hold sticks like hands."),
    ("Animal Parts", "Rabbit pelt", "Rabbits have nearly 360° vision with just a small blind spot in front of their noses."),
    ("Animal Parts", "Coyote tail", "Used as communication tools with different positions conveying specific messages."),
    ("Animal Parts", "Raccoon pelt", "Have 4-5 times more sensory receptors in front paws than back paws."),
    ("Animal Parts", "Bobcat Hyde", "Can leap up to 12 feet in a single bound; named for their short 'bobbed' tails."),
    ("Animal Parts", "Raccoon tail", "Ringed tail helps balance when climbing and serves as fat storage for winter."),
    ("Animal Parts", "Silver Fox hide", "Not a separate species but a color variant of red fox caused by genetic mutation."),
    ("Animal Parts", "Faun hide", "Young deer are born without scent to protect them from predators."),
    ("Animal Parts", "Woodboring Jewel Beatles", "Can detect forest fires from up to 50 miles away using heat-sensing organs."),
    
    # Bones & Skulls
    ("Bones & Skulls", "Giraffe vertebrae", "Giraffes have the same number of neck vertebrae as humans (7), but each is 10+ inches long."),
    ("Bones & Skulls", "Beaver skull", "Orange teeth contain iron compounds for strength and never stop growing."),
    ("Bones & Skulls", "Beaver jaw", "Powerful enough to cut through a 6-inch tree in under 15 minutes."),
    ("Bones & Skulls", "Fox skull", "Special adaptations allow foxes to pinpoint prey hiding under snow."),
    ("Bones & Skulls", "Hip bone", "Actually made of three separate bones that fuse during development."),
    ("Bones & Skulls", "Raccoon skull", "Raccoons can remember solutions to tasks for up to three years."),
    ("Bones & Skulls", "Deer jaw", "Teeth wear down over time, allowing experts to estimate a deer's age."),
    ("Bones & Skulls", "Deer bones", "The only mammals to completely regenerate an organ (antlers) annually."),
    ("Bones & Skulls", "Deer antler", "One of the fastest growing tissues, capable of growing up to an inch per day."),
    ("Bones & Skulls", "Fishbone tail", "Vertebrae designed to allow side-to-side movement while limiting up-and-down flexion."),
    ("Bones & Skulls", "Burmese python vertebrae", "Large pythons can have over 400 vertebrae for smooth movement and constriction."),
    ("Bones & Skulls", "Moose tooth", "Have specialized grinding molars but no upper front teeth, using a tough pad instead."),
    
    # Resin Replicas
    ("Resin Replicas", "Madagascar hissing cockroach", "Create their distinctive hiss by forcing air through specialized breathing tubes."),
    ("Resin Replicas", "Beaver teeth", "Grow continuously throughout life at about 4 inches per year."),
    ("Resin Replicas", "Beaver paw", "Hind feet are partially webbed with a split second toe used for grooming fur."),
    ("Resin Replicas", "Iguana head", "Have a third 'eye' on top of their head that detects light changes."),
    ("Resin Replicas", "Iguana foot", "Five toes with sharp claws help climb trees and dig burrows."),
    
    # Miscellaneous
    ("Miscellaneous", "Arrowheads", "Can be dated by shape, material, and technique; some over 12,000 years old."),
    ("Miscellaneous", "Clay bowl", "Often made waterproof by rubbing hot animal fat into the surface."),
]