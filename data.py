websites = {
    "Jared Coleman": "https://jaredraycoleman.com",
    "Evangelos Kranakis": "http://people.scs.carleton.ca/~kranakis/",
    "Oscar Morales-Ponce": "https://www.csulb.edu/college-of-engineering/dr-oscar-morales-ponce",
    "Jorge Urrutia": "https://www.matem.unam.mx/~urrutia/",
    "Birgit Vogtenhuber": "http://www.ist.tugraz.at/staff/vogtenhuber/",
    "Danny Krizanc": "https://dkrizanc.web.wesleyan.edu/",
    "Bhaskar Krishnamachari": "https://ceng.usc.edu/~bkrishna/",
    "Eugenio Grippo": "https://www.linkedin.com/in/eugenio-grippo-2574a31bb/",
    "Gunjan Verma": "https://ieeexplore.ieee.org/author/37886514800",

    "Tzanis Anevlavis": "https://www.linkedin.com/in/tzanis-anevlavis/",
    "Jonathan Bunton": "https://www.linkedin.com/in/jonathan-bunton-218a69126/",
    "Mine Dogan": "https://www.arni.ee.ucla.edu/people/mine-dogan/",
    # "Abel Souza": "",
    "Christina Fragouli": "https://www.ee.ucla.edu/christina-fragouli/",
    # "Matthew Maness": "",
    # "Karl Olson": "",
    "Prashant Shenoy": "https://people.cs.umass.edu/~shenoy/",
    "Paulo Tabuada": "http://www.seas.ucla.edu/~tabuada/",
    "Osama A Hanna": "https://www.arni.ee.ucla.edu/people/osama-hanna/",
    "Merve Karakas": "https://www.arni.ee.ucla.edu/people/merve-karakas/",
    "Xinlin Li": "https://www.arni.ee.ucla.edu/people/xinlin-li/",

    "Mehrdad Kiamari": "https://www.linkedin.com/in/mehrdad-kiamari-266b55132",
    "Lillian Clark": "https://lillyclark.github.io/",
    "Daniel D'Souza": "https://www.linkedin.com/in/daniel-d-souza-5802b4118",

    "Lorand Cheng": "https://www.linkedin.com/in/lorand-cheng/",

    "Hugo Embrechts": "https://www.linkedin.com/in/hugo-embrechts-443892",
    "Sulyab Thottungal Valapu": "https://sulyabtv.github.io/",
    "Tamoghna Sarkar": "https://tamoghna-sarkar.github.io/",
    "Anusha Avyukt": "https://anusha.rbind.io/",
    "Dimitri Torfs": "https://www.linkedin.com/in/dimitri-torfs-8a210a17/",
    "Michele Minelli": "https://micheleminelli.com/",

    "Ruben Rosales": "https://www.linkedin.com/in/ruben-rosales-99575b9b/",
    "Khalil Iskarous": "https://dornsife.usc.edu/profile/khalil-iskarous/",
}

pubs = [
    {
        "title": "LLM-Assisted Rule Based Machine Translation for Low/No-Resource Languages",
        "venue": "AmericasNLP @ NAACL 2024 - 4th Workshop on NLP for Indigenous Languages of the Americas",
        "authors": [
            "Jared Coleman",
            "Bhaskar Krishnamachari",
            "Khalil Iskarous",
            "Ruben Rosales",
        ],
        "links": {
            "pdf": "https://arxiv.org/pdf/2405.08997",
            "github": "https://github.com/kubishi/kubishi_sentences",
        },
        "abstract": (
            "We propose a new paradigm for machine translation that is particularly useful for no-resource languages (those without any publicly available bilingual or monolingual corpora): LLM-RBMT (LLM-Assisted Rule Based Machine Translation). Using the LLM-RBMT paradigm, we design the first language education/revitalization-oriented machine translator for Owens Valley Paiute (OVP), a critically endangered Indigenous American language for which there is virtually no publicly available data. We present a detailed evaluation of the translator's components: a rule-based sentence builder, an OVP to English translator, and an English to OVP translator. We also discuss the potential of the paradigm, its limitations, and the many avenues for future research that it opens up."
        )
    },
    {
        "title": "Linear Search for an Escaping Target with Unknown Speed",
        "venue": "IWOCA 2024 - 35th International Workshop on Combinatorial Algorithms",
        "authors": [
            "Jared Coleman",
            "Dmitry Ivanov",
            "Evangelos Kranakis",
            "Danny Krizanc",
            "Oscar Morales-Ponce"
        ],
        "links": {
            "pdf": "https://arxiv.org/abs/2404.14300",
        },
        "abstract": (
            "We consider linear search for an escaping target whose speed and initial position are unknown to the searcher. A searcher (an autonomous mobile agent) is initially placed at the origin of the real line and can move with maximum speed $1$ in either direction along the line. An oblivious mobile target that is moving away from the origin with an unknown constant speed $v<1$ is initially placed by an adversary on the infinite line at distance $d$ from the origin in an unknown direction. We consider two cases, depending on whether $d$ is known or unknown. The main contribution of this paper is to prove a new lower bound and give algorithms leading to new upper bounds for search in these settings. This results in an optimal (up to lower order terms in the exponent) competitive ratio in the case where $d$ is known and improved upper and lower bounds for the case where $d$ is unknown. Our results solve an open problem proposed in [Coleman et al., Proc. OPODIS 2022]"
        )
    },
    {
        "title": "Online Allocation of Sensing and Computation in Large Graphs",
        "venue": "IEEE CIC 2023 - International Conference on Collaboration and Internet Computing",
        "authors": [
            "Xinlin Li",
            "Merve Karakas",
            "Osama A Hanna",
            "Mehrdad Kiamari",
            "Jared Coleman",
            "Christina Fragouli",
            "Bhaskar Krishnamachari",
            "Gunjan Verma",
        ],
        "links": {
            "pdf": "https://ieeexplore.ieee.org/document/10429929",
            "github": "",
            # "linkedin": ""
        },
        "abstract": (
            "We consider vehicle tracking over a large territory equipped with sensors and computational units, and propose online resource allocation algorithms that decide which sensor nodes to activate, and on which computational units to perform the corresponding tracking tasks. We show through numerical evaluation that our approach can notably outperform state of art algorithms in terms of delay, communication cost, and the number of required sensor measurements."
        )
    },
    {
        "title": "DARSAN: A Decentralized Review System Suitable for NFT Marketplaces",
        "venue": "ICBC 2023 - International Conference on Blockchain",
        "authors": [
            "Sulyab Thottungal Valapu",
            "Tamoghna Sarkar",
            "Jared Coleman",
            "Anusha Avyukt",
            "Hugo Embrechts",
            "Dimitri Torfs",
            "Michele Minelli",
            "Bhaskar Krishnamachari"
        ],
        "links": {
            "pdf": "https://arxiv.org/pdf/2307.15768.pdf",
            "github": "",
            # "linkedin": ""
        },
        "abstract": (
            "We introduce DARSAN, a decentralized review system designed for Non-Fungible Token (NFT) marketplaces, to address the challenge of verifying the quality of highly resalable products with few verified buyers by incentivizing unbiased reviews. DARSAN works by iteratively selecting a group of reviewers (called \"experts\") who are likely to both accurately predict the objective popularity and assess some subjective quality of the assets uniquely associated with NFTs. The system consists of a two-phased review process: a \"pre-listing\" phase where only experts can review the product, and a \"pre-sale\" phase where any reviewer on the system can review the product. Upon completion of the sale, DARSAN distributes incentives to the participants and selects the next generation of experts based on the performance of both experts and non-expert reviewers. We evaluate DARSAN through simulation and show that, once bootstrapped with an initial set of appropriately chosen experts, DARSAN favors honest reviewers and improves the quality of the expert pool over time without any external intervention even in the presence of potentially malicious participants."
        )
    },
    {
        "title": "Search and Rescue on the Line",
        "venue": "SIROCCO 2023 - 30th International Colloquium on Structural Information and Communication Complexity",
        "authors": [
            "Jared Coleman",
            "Lorand Cheng",
            "Bhaskar Krishnamachari"
        ],
        "links": {
            "pdf": "https://anrg.usc.edu/www/papers/search_and_rescue.pdf",
            # "github": "",
            # "linkedin": ""
        },
        "abstract": (
                "We propose and study a problem inspired by a common task in disaster, military, and other emergency scenarios: search and rescue. "
                "Suppose an object (victim, message, target, etc.) is at some unknown location on a path. "
                "Given one or more mobile agents, also at initially arbitrary locations on the path, the goal is to find and deliver the object to a predefined destination in as little time as possible. "
                "We study the problem for the one- and two-agent cases and consider scenarios where the object and agents are arbitrarily (adversarially, even) placed along a path of either known (and finite) or unknown (and potentially infinite) length. "
                "We also consider scenarios where the destination is either at the endpoint or in the middle of the path. "
                "We provide both deterministic and randomized online algorithms for each of these scenarios and prove bounds on their (expected) competitive ratios."
        )
    },
    {
        "title": "Graph Convolutional Network-based Scheduler for Distributing Computation in the Internet of Robotic Things",
        "venue": "MILCOM 2023 WS-7 - Workshop On The Internet Of Things For Adversarial Environments",
        "authors": [
            "Jared Coleman",
            "Mehrdad Kiamari",
            "Lillian Clark",
            "Daniel D'Souza",
            "Bhaskar Krishnamachari"
        ],
        "links": {
            "pdf": "https://anrg.usc.edu/www/papers/edge_gcn_scheduler.pdf",
            "github": "https://github.com/ANRGUSC/gsdn",
            "linkedin": "https://www.linkedin.com/posts/jaredraycoleman_gsdn-summary-activity-7000586440682201088-vYEV?utm_source=share&utm_medium=member_desktop"
        },
        "abstract": (
            "Existing solutions for scheduling arbitrarily complex distributed applications on networks of computational nodes are insufficient for scenarios where the network topology is changing rapidly."
            "New Internet of Things (IoT) domains like the Internet of Robotic Things (IoRT) and the Internet of Battlefield Things (IoBT) demand solutions that are robust and efficient in  environments that experience constant and/or rapid change."
            "In this paper, we demonstrate how recent advancements in machine learning (in particular, in graph convolutional neural networks) can be leveraged to solve the task scheduling problem with decent performance and in much less time than traditional algorithms."
        )
    },
    {
        "title": "Delivery to Safety with Two Cooperating Robots",
        "venue": "SOFSEM 2023 - International Conference on Current Trends in Theory and Practice of Computer Science",
        "authors": [
            "Jared Coleman",
            "Evangelos Kranakis",
            "Danny Krizanc",
            "Oscar Morales-Ponce"
        ],
        "links": {
            "pdf": "https://arxiv.org/pdf/2210.04080",
        },
        "abstract": (
            "Two cooperating, autonomous mobile robots with arbitrary nonzero max speeds are placed at arbitrary initial positions in the plane. A remotely detonated bomb is discovered at some source location and must be moved to a safe distance away from its initial location as quickly as possible. In the Bomb Squad problem, the robots cooperate by communicating face-to-face in order to pick up the bomb from the source and carry it away to the boundary of a disk centered at the source in the shortest possible time. The goal is to specify trajectories which define the robots' paths from start to finish and their meeting points which enable face-to-face collaboration by exchanging information and passing the bomb from robot to robot."
            "We design algorithms reflecting the robots' knowledge about orientation and each other's speed and location. In the offline case, we design an optimal algorithm. For the limited knowledge cases, we provide online algorithms which consider robots' level of agreement on orientation as per OneAxis and NoAxis models, and knowledge of the boundary as per Visible, Discoverable, and Invisible. In all cases, we provide upper and lower bounds for the competitive ratios of the online problems."
        )
    },
    {
        "title": "The Snow Plow Problem: Perpetual Maintenance by Mobile Agents on the Line",
        "venue": "ICDCN 2023 - International Conference on Distributed Computing and Networking",
        "authors": [
            "Jared Coleman",
            "Oscar Morales-Ponce",
        ],
        "links": {
            "github": "https://github.com/jaredraycoleman/snow_plow"
        },
        "abstract": "We propose and study a new perpetual maintenance problem: The Snow Plow Problem. Inspired by snow removal in urban environments, we consider the perpetual maintenance by  n mobile agents of a fixed-length interval over which some resource accumulates continuously over time (i.e. snow). In order to maintain the interval, agents must traverse it, collecting accumulated resources by plowing over continuous segments, and then return to some predefined <i>destination</i> point on the interval to dump collected resources. In a sense, our problem can be described as a combination of the well-studied patrolling and delivery problems. The maintenance cost for an agent is some combination of the distance traveled and the volume of resources collected between visits to the destination. We first study the case where the maintenance cost is simply the maximum amount of snow each agent must carry at any point in time and provide an optimal $O(n)$ algorithm for computing optimal trajectories for the mobile agents for scenarios where the destination is at an endpoint and snow falls uniformly across the interval. Then, we generalize the problem for any maintenance cost which can be expressed as the product of a positive, non-decreasing travel cost function $f(x)$ (the cost to travel to a distance $x$) and a positive resource cost function $g(x)$ such that $\int_{y}^{z} g(x) dx$ represents the  volume of snowfall in one unit of time in the sub-interval $(y, z] \subseteq (0, 1]$. We provide a $(1+\epsilon)$-approximation algorithm that runs in $O(n \log 1/\epsilon )$ time and an exact $O(n)$ algorithm for the case where $f(x) = ax$ and $g(x) = b$ for some positive constants $a$ and $b$. Finally, we generalize further to consider scenarios where the destination is at any point along the interval, providing another $(1+\epsilon)$-approximation algorithm which runs in $O(n \log 1/\epsilon)$ time."
    },
    {
        "title": "Line Search for an Oblivious Moving Target",
        "venue": "OPODIS 2022 - International Conference on Principles of Distributed Systems",
        "authors": [
            "Jared Coleman",
            "Evangelos Kranakis",
            "Danny Krizanc",
            "Oscar Morales-Ponce"
        ],
        "links": {
            "pdf": "https://arxiv.org/pdf/2211.03686",
            "linkedin": "https://www.linkedin.com/posts/jaredraycoleman_line-search-for-an-oblivious-moving-target-activity-6999403018819428352-8xWQ?utm_source=share&utm_medium=member_desktop"
        },
        "abstract": (
            "Consider search on an infinite line involving an autonomous robot starting at the origin of the line and an oblivious moving target at initial distance $d \geq 1$ from it. The robot can change direction and move anywhere on the line with constant maximum speed 1 while the target is also moving on the line with constant speed $v>0$ but is unable to change its speed or direction. The goal is for the robot to catch up to the target in as little time as possible."
            "The classic case where $v=0$ and the target's initial distance d is moving <it>away</it> from the robot with a known speed $v<1$. In this paper we design and analyze search algorithms for the remaining possible knowledge situations, namely, when $d$ and $v$ are known, when $v$ is known but $d$ is unknown, when $d$ is known but $v$ is unknown, and when both $v$ and $d$ are unknown. Furthermore, for each of these knowledge models we consider separately the case where the target is moving away from the origin and the case where it is moving toward the origin. We design algorithms and analyze competitive ratios for all eight cases above. The resulting competitive ratios are shown to be optimal when the target is moving towards the origin as well as when $v$ is known and the target is moving away from the origin."
        )
    },
    {
        "title": "Multi-Objective Network Synthesis for Dispersed Computing in Tactical Environments",
        "venue": "SPIE Defense + Commercial Sensing",
        "authors": ["Jared Coleman", "Eugenio Grippo", "Bhaskar Krishnamachari", "Gunjan Verma"],
        "links": {
            "pdf": "https://anrg.usc.edu/www/papers/iobt.pdf",
            "github": "https://github.com/ANRGUSC/NSDC"
        },
        "abstract": (
            "Tactical operations like search and rescue or surveillance necessitate the rapid synthesis of physically dispersed assets and mobile compute nodes into a network capable of efficient and reliable information gathering, dissemination, and processing. We formalize this network synthesis problem as selecting one among a set of potentially deployable networks which optimally supports the distributed execution of complex applications. We propose a general framework for studying this type of problem and provide solutions for some well-motivated variants. We discuss how the framework can be extended to support other objectives, parameters, and constraints as well as more scalable solution approaches."
        )
    },
    {
        "title": "Network Synthesis for Tactical Environments: Scenario, Challenges, and Opportunities",
        "venue": "SPIE Defense + Commercial Sensing",
        "authors": [
            "Tzanis Anevlavis",
            "Jonathan Bunton",
            "Jared Coleman",
            "Mine Dogan",
            "Eugenio Grippo",
            "Abel Souza",
            "Christina Fragouli",
            "Bhaskar Krishnamachari",
            "Matthew Maness",
            "Karl Olson",
            "Prashant Shenoy",
            "Paulo Tabuada",
            "Gunjan Verma"
        ],
        "links": {
            "pdf": "https://anrg.usc.edu/www/papers/iobt_network_synthesis.pdf"
        },
        "abstract": (
            "We develop a network synthesis scenario, which is built around a concrete perimeter surveillance application, yet we believe captures a number of the challenges and requirements that are common to other tactical communication and computational network applications. The proposed scenario addresses the problem of binary population identification within a perimeter: our goal is to synthesize a sensing and computing network that classifies people moving within a given perimeter to one of two categories (e.g., friend or foe). We discuss several open challenges that we organize across the following clusters: sensor placement, communication network provisioning and optimization, computational task placement, dynamic resynthesis and resilience under adverserial settings. We also briefly discuss approaches that attempt to address such challenges."
        )
    },
    {
        "title": "Robotic Sorting on the Grid",
        "venue": "ICDCN 2022 - 23rd International Conference on Distributed Computing and Networking",
        "authors": ["Jared Coleman", "Oscar Morales-Ponce"],
        "links": {
            "pdf": "https://dl.acm.org/doi/pdf/10.1145/3491003.3491016"
        },
        "abstract": (
            "Inspired by robotic applications, we study the problem of sorting a set of items over a physical domain with mobile agents. Given m mobile robots and a grid where each cell contains a single element, the objective is to design algorithms that allow robots to cooperatively sort the elements over the grid in the minimum time. We assume a synchronous model where robots do not communicate, can carry up to c elements, and can move between adjacent cells in one unit of time (grab and release time is negligible). First, we show that any algorithm requires at least $\\Omega\\left(\\frac{n^2}{mc}\\right)$ units of time to sort an n-element line (an $n \\times 1$) and present an algorithm that sorts the elements in $O \\left(\\frac{n^2}{mc}\\right)$ time. Then, we show that any $n \\times 1$-grid requires at least $\\Omega \\left( \\frac{n^3}{mc} \\right)$ time and present an algorithm that completes in $O\\left(\\frac{n^3 \\log n}{mc}\\right)$ time. Our algorithms have an equivalent competitive ratio to Shear Sort [Isaacd et al., Proc ICPP 1986] with only $m=n$ agents (compared to the $n^2$ processors required by Shear Sort). Finally, we present experimental results that show the capacity has very little impact on the overall runtime and that a simplification of the algorithm leads to better results."
        )
    },
    {
        "title": "Message Delivery in the Plane by Robots with Different Speeds",
        "venue": "SSS 2021 - 23rd International Symposium on Stabilization, Safety, and Security of Distributed Systems",
        "authors": ["Jared Coleman", "Evangelos Kranakis", "Oscar Morales-Ponce", "Danny Krizanc"],
        "links": {
            "pdf": "https://arxiv.org/pdf/2109.12185"
        },
        "abstract": (
            "We study a fundamental cooperative message-delivery problem on the plane. Assume n robots which can move in any direction, are placed arbitrarily on the plane. Robots each have their own maximum speed and can communicate with each other face-to-face (i.e., when they are at the same location at the same time). There are also two designated points on the plane, $S$ (the <i>source</i>) and $D$ (the <i>destination</i>). The robots are required to transmit the message from the source to the destination as quickly as possible by face-to-face message passing. We consider both the offline setting where all information (the locations and maximum speeds of the robots) are known in advance and the online setting where each robot knows only its own position and speed along with the positions of $S$ and $D$."
            "In the offline case, we discover an important connection between the problem for two-robot systems and the well-known Apollonius circle which we employ to design an optimal algorithm. We also propose a $\\sqrt 2$ approximation algorithm for systems with any number of robots. In the online setting, we provide an algorithm with competitive ratio $\\frac 17 \\left( 5+ 4 \\sqrt{2} \\right)$ for two-robot systems and show that the same algorithm has a competitive ratio less than 2 for systems with any number of robots. We also show these results are tight for the given algorithm. Finally, we give two lower bounds (employing different arguments) on the competitive ratio of any online algorithm, one of 1.0391 and the other of 1.0405."
        )
    },
    {
        "title": "The Pony Express Communication Problem",
        "venue": "IWOCA 2021 - 32nd International Workshop on Combinatorial Algorithms",
        "authors": ["Jared Coleman", "Evangelos Kranakis", "Oscar Morales-Ponce", "Danny Krizanc"],
        "links": {
            "pdf": "https://arxiv.org/pdf/2105.03545"
        },
        "abstract": (
            "We introduce a new problem which we call the Pony Express problem. n robots with differing speeds are situated over some domain. A message is placed at some commonly known point. Robots can acquire the message either by visiting its initial position, or by encountering another robot that has already acquired it. The robots must collaborate to deliver the message to a given destination. The objective is to deliver the message in minimum time. In this paper we study the Pony Express problem on the line where n robots are arbitrarily deployed along a finite segment. The robots have different speeds and can move in both directions. We are interested in both offline centralized and online distributed algorithms. In the online case, we assume the robots have limited knowledge of the initial configuration. In particular, the robots do not know the initial positions and speeds of the other robots nor even their own position and speed. They do, however, know the direction on the line in which to find the message and have the ability to compare speeds when they meet.   "
            "First, we study the Pony Express problem where the message is initially placed at one endpoint of a segment and must be delivered to the other endpoint. We provide an $O(n \\log n)$ running time offline algorithm as well as an optimal online algorithm. Then we study the Half-Broadcast problem where the message is at the center and must be delivered to either one of the endpoints of the segment $O(n^2 \\log n)$ time and we provide an online algorithm that attains a competitive ratio of $\\frac 3 2$ which we show is the best possible. Finally, we study the Broadcast problem where the message is at the center and must be delivered to both endpoints of the segment $\\frac 9 5$, which we show is tight."
        )
    },
    {
        "title": "Minimizing The Maximum Distance Traveled To Form Patterns With Systems of Mobile Robots",
        "venue": "CCCG 2020, 32nd Canadian Conference on Computational Geometry, August 5-7, 2020",
        "authors": ["Jared Coleman", "Evangelos Kranakis", "Oscar Morales-Ponce", "Jorge Urrutia", "Birgit Vogtenhuber"],
        "links": {
            "pdf": "https://arxiv.org/pdf/2006.15664.pdf",
            "github": "https://github.com/jaredraycoleman/pafo",
            "youtube": "https://www.youtube.com/watch?v=Kq9y034tbiY"
        },
        "abstract": (
            "In the pattern formation problem, robots in a system must self-coordinate to form a given pattern, regardless of translation, rotation, uniform-scaling, and/or reflection. In other words, a valid final configuration of the system is a formation that is similar to the desired pattern. While there has been no shortage of research in the pattern formation problem under a variety of assumptions, models, and contexts, we consider the additional constraint that the maximum distance traveled among all robots in the system is minimum. Existing work in pattern formation and closely related problems are typically application-specific or not concerned with optimality (but rather feasibility). We show the necessary conditions any optimal solution must satisfy and present a solution for systems of three robots. Our work also led to an interesting result that has applications beyond pattern formation. Namely, a metric for comparing two triangles where a distance of 0 indicates the triangles are similar, and 1 indicates they are fully dissimilar."
        )
    }
]

projects = [
    {
        "name": 'GCN-Turtlebot',
        "links": {
            'youtube': 'https://www.youtube.com/watch?v=Lh5Tt8tOiDY',
            'linkedin': 'https://www.linkedin.com/feed/update/urn:li:activity:6932363615966572546/',
            'github': 'https://github.com/ANRGUSC/gcnschedule-turtlenet',
        },
        "description": (
            "<p><em>GCN-based Scheduler for Distributing Computation in the Internet of Robotic Things</em></p>" +
            "<p>This project explores how graph convolutional neural networks can be trained to immitate well-known task-graph scheduling algorithms for fast re-scheduling over networks with highly dynamic communication links. First-place winner of <a href='https://smile-sdsu.github.io/cps_iot22/'>The 2nd Student Design Competition on Networked Computing on the Edge</a> at <a href='https://cpsiotweek.neslab.it/'>CPS IoT Week 2022</a>.</p>"
        )
    },
    {
        "name": 'Tendermint Tutorial Demo',
        "links": {
            'youtube': 'https://www.youtube.com/watch?v=pVMFMiZGunw',
            'linkedin': 'https://www.linkedin.com/feed/update/urn:li:activity:6843577753867055104/',
            'github': 'https://github.com/ANRGUSC/tendermint_demo',
        },
        "description": (
            "<p>This is a short introductory tutorial on Tendermint consisting of a two-part video series and code to get started. Part 1 is a brief introduction to blockchain, Tendermint consensus, and the ABCI (Application Blockchain Interface). Part 2 is a tutorial demo which viewers can run themselves and follow along. No installation required - just click the 'Open with GitPod' in the <a href=\"https://github.com/ANRGUSC/tendermint_demo\">GitHub Repo</a>!"
        )
    },
    {
        "name": 'Kubishi',
        "links": {
            'facebook': 'https://facebook.com/kubishi',
            'instagram': 'https://instagram.com/ovkubishi',
            'twitter': 'https://twitter.com/ovkubishi',
            'github': 'https://github.com/kubishi/kubishi',
        },
        "description": "<p><em>Kubishi</em> is an online dictionary and encyclopedia for Owens Valley Paiute language and culture. The Owens Valley Paiute language is <a href='http://www.endangeredlanguages.com/lang/4692'>critically endangered</a>. <em>Kubishi</em> is one resource in the <a href='http://www.ovcdc.com/blog/language/'>fight</a> (led by Tribes of the Owens Valley) to reverse the damage inflicted by generations of forced assimilation and colonialism. The goal of this project is to help promote and preserve Owens Valley Paiute language and culture, but also to provide an open-source toolset for other tribal nations to do the same.</p>"
    }
]