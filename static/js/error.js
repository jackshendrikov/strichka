let isMobile = window.matchMedia("only screen and (max-width: 760px)").matches;

let fireflies;

if (isMobile) {
	fireflies = 40;
} else {
	fireflies = 100;
}

let $container = $(".container");
let $containerWidth = $container.width();
let $containerHeight = $container.height();

for (let i = 0; i < fireflies; i++) {
	let firefly = $('<div class="firefly"></div>');
	TweenLite.set(firefly, {
		x: Math.random() * $containerWidth,
		y: Math.random() * $containerHeight
	});
	$container.append(firefly);
	flyFirefly(firefly);
}

function flyFirefly(elm) {
	let fly = new TimelineMax();
	let fade = new TimelineMax({
		delay: Math.floor(Math.random() * 2) + 1,
		repeatDelay: Math.floor(Math.random() * 6) + 1,
		repeat: -1
	});

	fade.to(
		[elm],
		0.25,
		{ opacity: 0.25, yoyo: true, repeat: 1, repeatDelay: 0.2 },
		Math.floor(Math.random() * 6) + 1
	);

	fly
		.set(elm, {scale: Math.random() * 0.75 + 0.5})
		.to(elm, Math.random() * 100 + 100, {
			bezier: {
				values: [
					{
						x: Math.random() * $containerWidth,
						y: Math.random() * $containerHeight
					},
					{
						x: Math.random() * $containerWidth,
						y: Math.random() * $containerHeight
					}
					]
			},
			onComplete: flyFirefly,
			onCompleteParams: [elm]
		});
}
